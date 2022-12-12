# Import necessary frameworks
import tkinter as tk
import string
import secrets
import random
import pyperclip as pc

# Set up Application GUI
root = tk.Tk()
root.title("Password Generator")
root.geometry("300x160")
root.resizable(False, False)

# Create frames (Password Length radio buttons, and generate, clear, and exit buttons)
pwdLabelFrame = tk.LabelFrame(text="Choose a password length:", bd=1, width=100)
pwdLabelFrame.pack(pady=10)

# Create checkboxes
chVar12 = tk.IntVar()
check12 = tk.Checkbutton(pwdLabelFrame, text="12", variable=chVar12)
check12.grid(row=0, column=0, padx=10, sticky=tk.W)

chVar16 = tk.IntVar()
check16 = tk.Checkbutton(pwdLabelFrame, text="16", variable=chVar16)
check16.grid(row=0, column=1, padx=10, sticky=tk.W)

# Create generated password label
pwdEntry = tk.Entry(
    root, font=("Menlo", 12), state="normal", width=100, justify="center"
)
# pwdEntry.grid(row=2, column=0, padx=10, sticky=tk.W)
pwdEntry.pack(pady=10, padx=20)

# Create buttons frame
buttonFrame = tk.Frame(root)
buttonFrame.pack(pady=10)

# Define button function clear_input()
def clear_input():
    pwdEntry.delete(0, tk.END)
    chVar12.set(0)
    chVar16.set(0)


# Create clear button
buttonClear = tk.Button(buttonFrame, text="Clear", command=clear_input)
buttonClear.grid(row=2, column=2, sticky=tk.EW)

# Define button function exit
def exit():
    root.destroy()


# Create exit button
buttonExit = tk.Button(buttonFrame, text="Exit", command=exit)
buttonExit.grid(row=2, column=3, sticky=tk.EW)

# Shuffle password to make even more random
def shuffle(pwd=None):
    list_shuffled = list(pwd)
    random.shuffle(list_shuffled)
    pwd = "".join(list_shuffled)
    return pwd


# TODO: Ensure both checkboxes are NOT checked (radio button)
def check_fields():
    if chVar12.get() != 1 and chVar16.get() != 1:
        return True
    else:
        return False


# Generate a password
def generate_password():
    # Define variables
    uppercase_letters = string.ascii_letters.upper()
    lowercase_letters = string.ascii_letters.lower()
    digits = string.digits
    special_chars = string.punctuation
    alphabet = uppercase_letters + lowercase_letters + digits + special_chars

    # Define variable length based upon user input
    pwd_length = 0

    if check_fields() == True:
        pwdEntry.insert(index=0, string="Select a password length.")
    elif chVar12.get() == 1:
        pwd_length = 12
    elif chVar16.get() == 1:
        pwd_length = 16

    # Define empty string
    pwd = ""

    # Create for loop to add random choices from alphabet variable to password
    for i in range(pwd_length):
        pwd += "".join(secrets.choice(alphabet))
        shuffle(pwd=pwd)

    pwdEntry.insert(0, pwd)


# Create generate button
buttonGenerate = tk.Button(
    buttonFrame, text="Generate", command=generate_password, width=10
)
buttonGenerate.grid(row=2, column=0, sticky=tk.NSEW)

# Create copy function
def copy():
    # Get input of entry box which is displaying password
    entry = pwdEntry.get()
    pc.copy(entry)


# Create copy button
buttonCopy = tk.Button(buttonFrame, text="Copy", command=copy)
buttonCopy.grid(row=2, column=1, sticky=tk.NSEW)

root.mainloop()
