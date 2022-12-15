from setuptools import setup

APP = ["main.py"]
DATA_FILES = []
OPTIONS = {
    "argv_emulation": True,
    "packages": ["tkinter", "random", "pyperclip"],
    "iconfile": "app-icon.icns",
    "plist": {
        "CFBundleDevelopmentRegion": "English",
        "CFBundleIdentifier": "com.c0bras.xxx",
        "CFBundleVersion": "1.0.0",
    },
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
