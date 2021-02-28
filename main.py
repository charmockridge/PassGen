# Python 3.7.3

import string
from random import randint


# Function that checks if a password is secure
def Secure(genPass):
    # Checks if the generated password contains a lowercase letter
    checkLowercase = any(
        char in genPass for char in string.ascii_lowercase
    )

    # Checks if the generated password contains a uppercase letter
    checkUppercase = any(
        char in genPass for char in string.ascii_uppercase
    )

    # Checks if the generated password contains a number
    checkDigits = any(
        char in genPass for char in string.digits
    )

    # Checks if the generated password contains a symbol
    checkSymbols = any(
        char in genPass for char in string.punctuation
    )

    # Checks if all variables are True
    if (checkLowercase == checkUppercase == checkDigits ==
        checkSymbols == True):
        return True
    else:
        return False


# Function that generates the password
def Generate(passLen):
    # Generated letters will be appended
    generation = []
    # List containing upper and lowecase letters, numbers and symbols
    characters = (
        list(string.ascii_letters) +
        list(string.digits) +
        list(string.punctuation)
    )

    # Generates the password
    for i in range(0, passLen):
        indexChar = randint(0, len(characters) - 1)
        generation.append(characters[indexChar])

    # Checks if the password is strong. If not a new password is generated
    if Secure(generation) is False:
        return Generate(passLen)

    # Returns generated password
    return ''.join(str(x) for x in generation)


def Main():
    # Error handling if incorrect value is inputted
    try:
        passLen = int(input("How many characters in your password: "))

        password = Generate(passLen)

        print(f"\n==GENERATED PASSWORD==")
        print(password)
        print("======================")
    except ValueError:
        print("\nInvalid length! Please try again.\n")


if __name__ == "__main__":
    Main()
