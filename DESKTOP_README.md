# Van Anumodan — Desktop (full-capability) edition

The desktop edition runs a small processing engine on the PC so the app can do what a
tablet browser cannot: **OCR scanned documents in English *and* Hindi/Devanagari**, read
every proposal format, cross-check the figures, run **real GIS intersection** against
authoritative layers, and produce the report — with the officer only *verifying*, not typing.

Everything runs **locally on the machine**. No document or data is sent anywhere.

The same web interface is used; when the desktop engine is running, the **Documents** tab
shows *“Desktop engine connected (OCR: eng, hin)”* and uploads are processed by it. If the
engine is not running (e.g. the GitHub Pages version), the app quietly falls back to
browser mode for the machine-readable formats.

---

## System requirements

| | Minimum | Recommended |
|---|---|---|
| Operating system | Windows 10 (64-bit) | Windows 11 (64-bit) |
| CPU | Any 64-bit dual-core | Quad-core or better (faster OCR) |
| RAM | 8 GB | 16 GB (large scanned batches + GIS) |
| Free disk | ~1.5 GB | 2 GB+ |
| Internet | **Not required to run** | Needed only to first download/build, fetch rule updates, or open source links |

- **OCR** uses Tesseract with the **English + Hindi** language packs. In the single-EXE build these are bundled; for the Python route they are installed once.
- **GIS intersection** needs the authoritative layers (Protected Area / ESZ / Tiger Reserve etc.) as **GeoJSON or KML**, supplied by you.
- The engine also runs on **macOS and Linux** (it is standard Python), but the ready-made installer below targets Windows.

---

## Option A — Single `VanAnumodan.exe` (recommended for officers)

No Python, no setup. OCR is built in.

1. Get `VanAnumodan.exe` (see “Producing the EXE” below).
2. Double-click it. A console window opens and your browser opens the app automatically.
3. Use it. To stop, close the console window.

## Option B — Run with Python (for a technical user, or to try it quickly)

1. Install **Python 3.11+** (tick *“Add python.exe to PATH”* during install).
2. Install **Tesseract-OCR for Windows** (UB Mannheim build) and tick **Hindi** during
   setup — this enables OCR. (Skip only if you don’t need scanned-document reading.)
3. Double-click **`desktop\run_windows.bat`**. On first run it sets up its own environment
   and then launches; the browser opens automatically.

---

## Producing the EXE

**Easiest — GitHub builds it for you (no Windows dev setup):**
The repository includes `.github/workflows/build-windows.yml`. When you push to `main`,
GitHub Actions builds a self-contained `VanAnumodan.exe` (Tesseract + Hindi bundled) and
uploads it under the run’s **Artifacts**. Push a version tag (e.g. `v1.0.0`) and it is also
attached to a **Release** for easy download.

**Or build locally on a Windows PC:**
Install Python 3.11+ and Tesseract-OCR, then run **`desktop\build_exe.bat`**. The result is
`desktop\dist\VanAnumodan.exe`.

---

## How to use

1. Launch the app (Option A or B). Open the **Documents** tab — it should say
   *“Desktop engine connected”* with the OCR languages listed.
2. **Drop all the proposal files together** (or a single ZIP/KMZ). The engine:
   - OCRs scanned PDFs and images (English + Hindi),
   - reads spreadsheets, Word and digital PDFs,
   - computes the KML/KMZ area,
   - pulls the forest-area / CA / tree figures and lists what each file yielded.
3. **Apply to reconciliation** to pre-fill the grid, then **verify** the values.
4. Generate the **Intake & Extraction Report**, then complete the checklist and the
   **Executive Scrutiny Report** as usual.

### GIS intersection (built in)
The engine checks the proposal boundary against authoritative layers **automatically**.

1. Put your layer files (GeoJSON or KML/KMZ) in the **`layers/`** folder next to the app
   (or point the `VA_LAYERS_DIR` environment variable at any folder). Name them so the
   category is clear — `tiger_reserve.geojson`, `esz_uttarakhand.kml`,
   `sanctuaries.geojson`, `corridors.geojson` — or add a `manifest.json` to set categories
   explicitly (see `desktop/layers/manifest.example.json`).
2. In the app, **GIS tab → Check against folder layers**: it computes the boundary area and
   intersects it against every layer in the folder, filling the GIS checklist rows. You can
   also attach layers ad-hoc in the four labelled slots and use **Run spatial check**.

**Automatic red flags:** if the proposal intersects a **Tiger Reserve / CTH** or a
**Protected Area**, a **Critical** red flag is raised automatically — which blocks a
“Ready for Forwarding” verdict until addressed. An **ESZ** or **corridor** intersection
raises a **Major** flag. Flags auto-close if a later check shows no intersection. Officers
still record the Pass/Fail assessment on the GIS checklist.

---

## Privacy & accuracy

- All processing is **on the local machine**; nothing is uploaded.
- **OCR is assistive, not authoritative.** Machine-read figures — especially from scanned or
  stamped pages — must be **verified by the officer** before they inform any finding. The
  Intake report always states which documents were OCR’d.
- Keep the PC and any exported case files under the same care as official records.

---

## Two editions, one app

| | Browser / PWA (GitHub Pages) | Desktop (this) |
|---|---|---|
| Install | Add to Home Screen | EXE or Python |
| KML / spreadsheet / Word / digital PDF | ✓ | ✓ |
| **Scanned PDF / image OCR (Eng + Hindi)** | ✕ | **✓** |
| **Real GIS intersection** | ✕ | **✓** |
| Runs offline | ✓ | ✓ |
| Best for | quick access, field/tablet | full scrutiny on a PC |
