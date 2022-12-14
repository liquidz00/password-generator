# Import necessary frameworks
import tkinter as tk
import string
import secrets
import random
import pyperclip as pc

# Set up Application GUI
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x200")
root.resizable(False, False)

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# ** Create all frames (pwdLabel, middleFrame, buttonFrame) **

# pwdLabelFrame
pwdLabelFrame = tk.LabelFrame(root, text="Choose a password length:", bd=1)
pwdLabelFrame.grid(row=0, column=0, pady=10, padx=15, sticky=tk.NSEW)

# middleFrame
middleFrame = tk.Frame(root, relief="flat")
middleFrame.grid(row=1, column=0, pady=10, padx=15, sticky=tk.NSEW)

# buttonFrame
buttonFrame = tk.Frame(root)
buttonFrame.grid(row=2, column=0, pady=10, padx=15, sticky=tk.NSEW)

# buttonFrame grid customization
buttonFrame.grid_columnconfigure(1, weight=2)


# ** TOP FRAME WIDGETS **
chVar12 = tk.IntVar()
check12 = tk.Checkbutton(pwdLabelFrame, text="12", variable=chVar12)
check12.grid(row=0, column=0, pady=10, padx=15, sticky=tk.W)

chVar16 = tk.IntVar()
check16 = tk.Checkbutton(pwdLabelFrame, text="16", variable=chVar16)
check16.grid(row=0, column=1, pady=10, padx=15, sticky=tk.W)


# ** MIDDLE FRAME WIDGETS **
entryVar = tk.StringVar()
pwdEntry = tk.Entry(
    middleFrame, font=("Menlo", 12), justify="left", textvariable=entryVar, width=40
)
pwdEntry.grid(row=0, column=0, sticky=tk.W)

# Copy function
def copy():
    # Get input of entry box which is displaying password
    if pwdEntry.get() != "":
        entry = pwdEntry.get()
        pc.copy(entry)
        errorLabel.config(text="Password copied!", fg="Green")
        buttonCopy.config(image=None, text="✔️")
    else:
        buttonCopy.config(state="disabled")


# Create copy button
copyImage = tk.PhotoImage(file="copy-30.png")
buttonCopy = tk.Button(
    middleFrame,
    image=copyImage,
    command=copy,
    state="disabled",
    width=20,
    height=20,
)
buttonCopy.grid(row=0, column=1, sticky=tk.W)

# Create error label
errorLabel = tk.Label(middleFrame, text="", justify="left", font=("Helvetica", 12))
errorLabel.grid(row=1, column=0, sticky=tk.W)


# ** BOTTOM FRAME WIDGETS **

# Define button function clear_input()
def clear_input():
    pwdEntry.delete(0, tk.END)
    chVar12.set(0)
    chVar16.set(0)
    errorLabel.config(text="")
    buttonState()


# Create clear button
buttonClear = tk.Button(buttonFrame, text="Clear", command=clear_input)
buttonClear.grid(row=0, column=3, sticky=tk.W)

# Define exit function
def exit():
    root.destroy()


# Create exit button
buttonExit = tk.Button(buttonFrame, text="Exit", command=exit)
buttonExit.grid(row=0, column=4, sticky=tk.W)

# Create generate function
def generate_password():

    # Clear password entry if string is present
    if pwdEntry.get() != "":
        pwdEntry.delete(0, tk.END)
        errorLabel.config(text="")

    # Define variables
    uppercase_letters = string.ascii_letters.upper()
    lowercase_letters = string.ascii_letters.lower()
    digits = string.digits
    special_chars = string.punctuation
    alphabet = uppercase_letters + lowercase_letters + digits + special_chars

    # Define variable length based upon user input
    pwd_length = 0

    if check_fields() == True:
        errorLabel.config(text="Select a password length.", fg="Red")
    elif check_fields() == None:
        errorLabel.config(text="Error: both lengths selected.", fg="Red")
    elif chVar12.get() == 1:
        pwd_length = 12
        errorLabel.config(text="")
    elif chVar16.get() == 1:
        pwd_length = 16
        errorLabel.config(text="")

    # Define empty string
    pwd = ""

    # Create for loop to add random choices from alphabet variable to password
    for i in range(pwd_length):
        pwd += "".join(secrets.choice(alphabet))
        shuffle(pwd=pwd)

    # Insert generated password into text entry
    pwdEntry.insert(0, pwd)
    buttonState()


# Create generate button
buttonGenerate = tk.Button(
    buttonFrame,
    text="Generate",
    command=generate_password,
    width=15,
)
buttonGenerate.grid(row=0, column=0, sticky=tk.E)

# ** Additional Functions **

# Shuffle password to make even more random
def shuffle(pwd=None):
    list_shuffled = list(pwd)
    random.shuffle(list_shuffled)
    pwd = "".join(list_shuffled)
    return pwd


# Ensure both checkboxes are NOT checked (radio button)
def check_fields():
    if chVar12.get() != 1 and chVar16.get() != 1:
        return True
    elif chVar12.get() == 1 and chVar16.get() == 1:
        return None
    else:
        return False


# Create function to disable/enable buttons
def buttonState(*args):
    if entryVar.get() != "":
        buttonCopy.config(state="normal")
    else:
        buttonCopy.config(state="disabled")


root.mainloop()
