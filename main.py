# Import necessary frameworks
import secrets
import string
import random
from shuffler import shuffle

# Create main function
def main():
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
    pwd = ""

    # Create for loop to add random choices from alphabet variable to password
    for char in range(pwd_length):
        pwd += "".join(secrets.choice(alphabet))

    # Shuffle output to verify password does not fit a unique pattern
    shuffle(pwd)

    # Show user generated password
    print(pwd)


while True:
    main()
    # Restart process or end
    response = input("Generate another password? (Y/N) ").strip().lower()
    match response:
        case "y":
            True
        case "n":
            print("Goodbye")
            break
        case other:
            print("Please enter either Y or N")
