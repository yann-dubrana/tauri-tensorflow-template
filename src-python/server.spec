# tensorflow-server-x86_64-pc-windows-msvc.spec
# PyInstaller configuration for the FastAPI tensorflow-server-x86_64-pc-windows-msvc

a = Analysis(
    ["main.py"],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    [],  # Remove a.binaries, a.zipfiles, a.datas from here
    exclude_binaries=True,  # Add this line
    name="tensorflow-server-x86_64-pc-windows-msvc",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True
)

# Add COLLECT to bundle files in a directory
COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='tensorflow-server-x86_64-pc-windows-msvc'
)