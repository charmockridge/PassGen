import string
from random import randint


def Secure(genPass):
    checkLowercase = any(
        char in genPass for char in string.ascii_lowercase
    )

    checkUppercase = any(
        char in genPass for char in string.ascii_uppercase
    )

    checkDigits = any(
        char in genPass for char in string.digits
    )

    checkSymbols = any(
        char in genPass for char in string.punctuation
    )

    if (checkLowercase == checkUppercase == checkDigits ==
        checkSymbols == True):
        return True
    else:
        return False


def Generate(passLen):
    generation = []
    characters = (
        list(string.ascii_letters) +
        list(string.digits) +
        list(string.punctuation)
    )

    print(password)

    for i in range(0, passLen):
        indexChar = randint(0, len(characters) - 1)
        generation.append(characters[indexChar])

    password = ''.join(str(x) for x in password)
    print(generation)
    print("=" + password)
    check = Secure(generation)

    # Error here
    if check is True:
        return password
    elif check is False:
        Generate(passLen)


def Main():
    try:
        passLen = int(input("How many characters in your password: "))
        password = Generate(passLen)

        print("\n==GENERATED PASSWORD==")
        print(password)
        print("======================")
    except ValueError:
        print("\nInvalid length! Please try again.\n")


if __name__ == "__main__":
    Main()
