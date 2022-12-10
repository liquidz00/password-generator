import PySimpleGUI as sg
from main import main


def gui():
    # Show user window
    sg.theme("Reddit")
    titlebar = sg.Titlebar("Password Generator")

    layout = [
        [sg.Text("How many characters long? Choose 12 or 16")],
        [sg.Checkbox("12", default=True)],
        [sg.Checkbox("16")],
        [sg.InputText(key="pwd")],
        [sg.Button("Generate"), sg.Button("Clear"), sg.Exit()],
    ]

    window = sg.Window(titlebar, layout)


def clear_input():
    for key in main.values:
        gui.window[key]("")
    return None
