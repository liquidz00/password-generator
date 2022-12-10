# Import necessary frameworks
from shuffler import shuffle
from generator import generate
from gui import gui, clear_input


# Create main function
def main():
    # Create a password using generate function
    pwd = generate()

    # Shuffle output to verify password does not fit a unique pattern
    shuffle(pwd)

    # Show user generated password
    print(pwd)


while True:
    main()
    event, values = gui.window.read()
    if event == gui.sg.WIN_CLOSED or event == "Exit":
        gui.window.close()
        break
    if event == "Clear":
        gui.clear_input()
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
