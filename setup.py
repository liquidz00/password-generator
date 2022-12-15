from setuptools import setup

APP = ["main.py"]
DATA_FILES = ["app-icon.icns", "copy-30.png"]
OPTIONS = {
    "argv_emulation": True,
    "iconfile": "app-icon.icns",
    "packages": ["tkinter", "pyperclip", "string", "secrets", "random", "os"],
    "includes": ["tkinter", "pyperclip", "string", "secrets", "random", "os"],
    "plist": {
        "CFBundleName": "Password Generator",
        "CFBundleDisplayName": "Password Generator",
        "CFBundleGetInfoString": "Generate Passwords",
        "CFBundleIdentifier": "com.c0bras.passwordgenerator",
        "CFBundleVersion": "1.0.0",
        "CFBundleShortVersionString": "1.0.0",
    },
}

setup(
    app=APP,
    name="Password Generator",
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
