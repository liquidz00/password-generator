import secrets
import string

loop = 0

while loop == 0:
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    alphabet = letters + digits + special_chars

    pwd_length = int(input("How many characters long? Choose 12 or 16: "))
    match pwd_length:
        case 12:
            pwd_length = 12
        case 16:
            pwd_length = 16
        case other:
            print("Please enter either 12 or 16")

    pwd = ""
    for char in range(pwd_length):
        pwd += "".join(secrets.choice(alphabet))

    print(pwd)
    print("Would you like to generate another password? [Y/N]")
    response = str(input()).lower()
    match response:
        case "y":
            loop = 0
        case "n":
            loop = 1

    # if (
    #     any(char in special_chars for char in pwd)
    #     and sum(char in digits for char in pwd) >= 2
    # ):
    #     break
