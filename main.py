import secrets
import string

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars

pwd_length = int(input("How many characters long? Choose 12 or 16: "))
match pwd_length:
    case 12:
        print("Your number is 12")
    case 16:
        print("Your number is 16")
    case other:
        print("Please enter either 12 or 16")
