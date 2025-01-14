# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['ids_tespit.py'],
    pathex=[],
    binaries=[],
    datas=[('MODEL', 'MODEL'), ('MODEL_HASSAS', 'MODEL_HASSAS')],
    hiddenimports=['pandas', 'os', 'time', 'sklearn', 'sklearn.utils._cython_blas', 'sklearn.ensemble._forest', 'numpy.core.multiarray', 'joblib'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='ids_tespit',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
