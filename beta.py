import tkinter as tk
import customtkinter as ctk
import string
import secrets
import random
import pyperclip as pc
import os

# Set default CTK properties
ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme(
    "blue"
)  # Themes: "blue" (standard), "green", "dark-blue", "orange" (in progress)

# Factor code into class
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Set up Application GUI
        self.title("Password Generator")
        self.geometry("350x200")
        self.resizable(False, False)

        # Configure grid accordingly
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # CREATE ALL FRAMES

        # pwdLabelFrame
        pwdLabelFrame = tk.LabelFrame(self, text="Choose a password length:", bd=1)
        pwdLabelFrame.grid(row=0, column=0, pady=10, padx=15, sticky=tk.NSEW)

        # middleFrame
        middleFrame = ctk.CTkFrame(self)
        middleFrame.grid(row=1, column=0, pady=10, padx=15, sticky=tk.NSEW)

        # buttonFrame
        buttonFrame = ctk.CTkFrame(self)
        buttonFrame.grid(row=2, column=0, pady=10, padx=15, sticky=tk.NSEW)

        # buttonFrame grid customization
        buttonFrame.grid_columnconfigure(1, weight=2)

        # CREATE TOP FRAME WIDGETS
        chVar12 = tk.IntVar()
        check12 = ctk.CTkCheckBox(pwdLabelFrame, text="12", variable=chVar12)
        check12.grid(row=0, column=0, pady=10, padx=15, sticky=tk.W)

        chVar16 = ctk.IntVar()
        check16 = ctk.CTkCheckBox(pwdLabelFrame, text="16", variable=chVar16)
        check16.grid(row=0, column=1, pady=10, padx=15, sticky=tk.W)

        # CREATE MIDDLE FRAME WIDGETS
        entryVar = ctk.StringVar()
        pwdEntry = ctk.CTkEntry(
            middleFrame,
            font=("Menlo", 12),
            justify="left",
            textvariable=entryVar,
            width=40,  # width=30 for PC
        )
        pwdEntry.grid(row=0, column=0, sticky=tk.W)


if __name__ == "__main__":
    app = App()
    app.mainloop()
