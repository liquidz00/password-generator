# Import necessary frameworks
from shuffler import shuffle
from generator import generate

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
