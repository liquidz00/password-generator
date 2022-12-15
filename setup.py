from setuptools import setup

APP = ["main.py"]
DATA_FILES = ["app-icon.icns", "copy-30.png"]
OPTIONS = {
    "argv_emulation": True,
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
