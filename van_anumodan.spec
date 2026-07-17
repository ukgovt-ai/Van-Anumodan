# PyInstaller spec for Van Anumodan desktop
import os
from PyInstaller.utils.hooks import collect_submodules

datas = [('web', 'web')]
# self-contained OCR if Tesseract was vendored by build_exe.bat / CI
if os.path.isdir('vendor/tesseract'):
    datas.append(('vendor/tesseract', 'tesseract'))

hiddenimports = (collect_submodules('uvicorn')
                 + ['fastapi', 'shapely', 'shapely.geometry', 'PIL', 'fitz',
                    'openpyxl', 'docx', 'pytesseract', 'multipart'])

a = Analysis(['app.py'], pathex=['.'], binaries=[], datas=datas,
             hiddenimports=hiddenimports, hookspath=[], runtime_hooks=[], excludes=[])
pyz = PYZ(a.pure)
exe = EXE(pyz, a.scripts, a.binaries, a.datas, [], name='VanAnumodan',
          console=True, icon=None, upx=False)
