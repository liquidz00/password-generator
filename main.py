# Import necessary frameworks
import tkinter as tk
import string
import secrets
import random

# Set up Application GUI
root = tk.Tk()
root.title("Password Generator")

# Create checkboxes
chVar12 = tk.IntVar()
check12 = tk.Checkbutton(root, text="12", variable=chVar12)
check12.grid(row=0, column=0, sticky=tk.W)

chVar16 = tk.IntVar()
check16 = tk.Checkbutton(root, text="16", variable=chVar16)
check16.grid(row=1, column=0, sticky=tk.W)

# Create generated password label
pwdLabel = tk.Label(root)
pwdLabel.grid(row=2, column=0, sticky=tk.W)

# Define button function clear_input()
def clear_input():
    pwdLabel.config(text="")
    chVar12.set(0)
    chVar16.set(0)


# Create clear button
buttonClear = tk.Button(root, text="Clear", command=clear_input)
buttonClear.grid(row=3, column=1, sticky=tk.W)

# Define button function exit
def exit():
    root.destroy()


# Create exit button
buttonExit = tk.Button(root, text="Exit", command=exit)
buttonExit.grid(row=3, column=2, sticky=tk.W)


def generate_password():
    # Define variables
    uppercase_letters = string.ascii_letters.upper()
    lowercase_letters = string.ascii_letters.lower()
    digits = string.digits
    special_chars = string.punctuation
    alphabet = uppercase_letters + lowercase_letters + digits + special_chars

    # Define variable length based upon user input
    pwd_length = 0

    if chVar12.get() == 1:
        pwd_length = 12
    elif chVar16.get() == 1:
        pwd_length = 16
    else:
        pwdLabel.config(text="Please select either 12 or 16")

    # Define empty string
    pwd = ""

    # Create for loop to add random choices from alphabet variable to password
    for char in range(pwd_length):
        pwd += "".join(secrets.choice(alphabet))

    pwdLabel.config(text=pwd)


# Create generate button
buttonGenerate = tk.Button(root, text="Generate", command=generate_password)
buttonGenerate.grid(row=3, column=0, sticky=tk.W)


def shuffle(pwd=None):
    list_shuffled = list(pwd)
    random.shuffle(list_shuffled)
    pwd = "".join(list_shuffled)
    return pwd


root.mainloop()
