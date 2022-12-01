# Import necessary frameworks
import secrets
import string
import random

# Create loop variable for while loop
loop = 0

# Set up while loop
while loop == 0:

    # Define variables
    uppercase_letters = string.ascii_letters.upper()
    lowercase_letters = string.ascii_letters.lower()
    digits = string.digits
    special_chars = string.punctuation
    alphabet = uppercase_letters + lowercase_letters + digits + special_chars

    # Define variable length based upon user input
    pwd_length = int(input("How many characters long? Choose 12 or 16: "))

    # Assign value based upon user's response
    match pwd_length:
        case 12:
            pwd_length = 12
        case 16:
            pwd_length = 16
        case other:
            print("Please enter either 12 or 16")

    # Define empty string
    temp_pwd = ""

    # Create for loop to add random choices from alphabet variable to password
    for char in range(pwd_length):
        temp_pwd += "".join(secrets.choice(alphabet))

    list_shuffled = list(temp_pwd)
    random.shuffle(list_shuffled)
    pwd = "".join(list_shuffled)

    # Show user generated password
    print(pwd)

    # Restart process or end
    print("Would you like to generate another password? [Y/N]")

    # Define response variable
    response = str(input()).lower()

    # Match response
    match response:
        case "y":
            loop = 0
        case "n":
            loop = 1

    # TODO: Set up extra constraints for password
