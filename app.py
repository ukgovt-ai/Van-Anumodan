"""
Van Anumodan — local desktop server.
Serves the Van Anumodan web UI at http://127.0.0.1:8756 and exposes a local API
that does the heavy processing (OCR of scanned English/Hindi documents, PDF/DOCX/
spreadsheet/KML parsing, GIS intersection). Everything runs on this machine; no
data is sent anywhere.
"""
import os, sys, threading, webbrowser
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

import extractor

APP_NAME = "Van Anumodan"
HOST, PORT = "127.0.0.1", 8756

def _web_dir():
    # PyInstaller bundle
    if hasattr(sys, "_MEIPASS"):
        p = os.path.join(sys._MEIPASS, "web")
        if os.path.isdir(p):
            return p
    here = os.path.dirname(os.path.abspath(__file__))
    for cand in (os.path.join(here, "web"), os.path.dirname(here), here):
        if os.path.isfile(os.path.join(cand, "index.html")):
            return cand
    return here

WEB = _web_dir()

def _layers_dir():
    d = os.environ.get("VA_LAYERS_DIR")
    if d:
        return d
    base = os.path.dirname(sys.executable) if getattr(sys, "frozen", False) else os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, "layers")

api = FastAPI(title=APP_NAME)

@api.get("/api/health")
def health():
    langs = []
    try:
        import pytesseract
        langs = pytesseract.get_languages(config="")
    except Exception:
        pass
    ld = _layers_dir()
    return {"ok": True, "app": APP_NAME, "engine": "desktop",
            "ocr": bool(langs), "ocr_langs": langs,
            "layers_dir": ld, "layers_count": len(extractor.list_layers(ld))}

@api.get("/api/layers")
def layers_list():
    d = _layers_dir()
    return {"dir": d, "layers": extractor.list_layers(d)}

@api.post("/api/gis-auto")
async def gis_auto_ep(kml: UploadFile = File(...)):
    data = await kml.read()
    return JSONResponse(extractor.gis_auto(data, _layers_dir()))

@api.post("/api/extract")
async def extract(files: list[UploadFile] = File(...)):
    records = []
    for f in files:
        data = await f.read()
        records.extend(extractor.process_file(f.filename, data))
    return JSONResponse({"records": records})

@api.post("/api/gis-check")
async def gis(kml: UploadFile = File(...), layers: list[UploadFile] = File(default=[])):
    kml_bytes = await kml.read()
    layer_data = [(l.filename, await l.read()) for l in layers]
    return JSONResponse(extractor.gis_check(kml_bytes, layer_data))

# serve the web UI (index.html at "/")
@api.get("/")
def root():
    return FileResponse(os.path.join(WEB, "index.html"))

api.mount("/", StaticFiles(directory=WEB, html=True), name="web")

def _open_browser():
    webbrowser.open(f"http://{HOST}:{PORT}/")

def main():
    print(f"\n  {APP_NAME} desktop engine")
    print(f"  Serving UI from: {WEB}")
    print(f"  Open:  http://{HOST}:{PORT}/\n  (Close this window to stop.)\n")
    threading.Timer(1.2, _open_browser).start()
    uvicorn.run(api, host=HOST, port=PORT, log_level="warning")

if __name__ == "__main__":
    main()
