from setuptools import setup

APP = ["main.py"]
DATA_FILES = ["app-icon.icns", "copy-30.png"]
OPTIONS = {
    "argv_emulation": True,
    "iconfile": "app-icon.icns",
    "packages": ["tkinter", "pyperclip"],
}

setup(
    app=APP,
    name="Password Generator",
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
