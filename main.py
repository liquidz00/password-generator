# Import necessary frameworks
from shuffler import shuffle
from generator import generate
import PySimpleGUI as sg

# Create main function
def main():
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
        for key in values:
            window[key]("")
        return None

    # Create a password using generate function
    pwd = generate()

    # Shuffle output to verify password does not fit a unique pattern
    shuffle(pwd)

    # Show user generated password
    print(pwd)


while True:
    main()
    event, values = main.window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        main.window.close()
        break
    if event == "Clear":
        main.clear_input()
    if event == "Generate":
        generate()
        shuffle()

    # response = input("Generate another password? (Y/N) ").strip().lower()
    # match response:
    #     case "y":
    #         True
    #     case "n":
    #         print("Goodbye")
    #         break
    #     case other:
    #         print("Please enter either Y or N")
