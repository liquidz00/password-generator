# Import necessary frameworks
# import _functions as pwdf
import PySimpleGUI as sg
import string
import secrets
import random


# Show user window
sg.theme("Reddit")
titlebar = sg.Titlebar("Password Generator")

layout = [
    [sg.Text("How many characters long? Choose 12 or 16")],
    [sg.Checkbox("12", default=False, enable_events=True, key="__12pwd__")],
    [sg.Checkbox("16", default=False, enable_events=True, key="__16pwd__")],
    [sg.InputText(key="__PWD__")],
    [
        sg.Button("Generate", enable_events=True, key="Generate"),
        sg.Button("Clear"),
        sg.Exit(),
    ],
]

window = sg.Window(titlebar, layout)


def generate_password():
    # Define variables
    uppercase_letters = string.ascii_letters.upper()
    lowercase_letters = string.ascii_letters.lower()
    digits = string.digits
    special_chars = string.punctuation
    alphabet = uppercase_letters + lowercase_letters + digits + special_chars

    # Define variable length based upon user input
    pwd_length = 0

    # if layout.values["12 pwd"] == True:
    #     pwd_length = 12
    # elif layout.values["16 pwd"] == True:
    #     pwd_length = 16

    # Assign value based upon user's response
    # match pwd_length:
    #     case 12:
    #         pwd_length = 12
    #     case 16:
    #         pwd_length = 16
    #     case other:
    #         print("Please enter either 12 or 16")

    # Define empty string
    pwd = ""

    # Create for loop to add random choices from alphabet variable to password
    for char in range(pwd_length):
        pwd += "".join(secrets.choice(alphabet))

    return pwd


def shuffle(pwd=None):
    list_shuffled = list(pwd)
    random.shuffle(list_shuffled)
    pwd = "".join(list_shuffled)
    return pwd


def clear_input():
    for key in values:
        window[key]("")
    return None


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "Clear":
        print("information cleared")
        clear_input()
    if event == "Generate":
        pwd = generate_password()
        shuffle(pwd)
        window.update(values[pwd])


window.close()
