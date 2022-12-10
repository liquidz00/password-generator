# Import necessary frameworks
import pwd_functions as pwdf
import PySimpleGUI as sg


# Show user window
sg.theme("Reddit")
titlebar = sg.Titlebar("Password Generator")

layout = [
    [sg.Text("How many characters long? Choose 12 or 16")],
    [sg.Checkbox("12", default=False, enable_events=True, key="12 pwd")],
    [sg.Checkbox("16", default=False, enable_events=True, key="16 pwd")],
    [sg.InputText(key="pwd")],
    [
        sg.Button("Generate", enable_events=True, key="Generate"),
        sg.Button("Clear"),
        sg.Exit(),
    ],
]

window = sg.Window(titlebar, layout)

# # Create a password using generate function
# pwd = generate()

# # Shuffle output to verify password does not fit a unique pattern
# shuffle(pwd)

# # Show user generated password
# print(pwd)


def clear_input():
    for key in values:
        window[key]("")


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        window.close()
        break
    if event == "Clear":
        print("information cleared")
        pwdf.clear_input()
    if event == "Generate":
        print("Generate clicked")
        # generate()
        # shuffle()
