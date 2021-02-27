import string
from random import randint


def Generate(passLen):
    password = []
    characters = (
        list(string.ascii_letters) +
        list(string.digits) +
        list(string.punctuation)
    )

    for i in range(0, passLen):
        indexChar = randint(0, len(characters) - 1)
        password.append(characters[indexChar])

    return str("".join(str(x) for x in password))


def Main():
    try:
        passLen = int(input("How many characters in your password: "))
        Generate(passLen)
    except ValueError:
        print("\nInvalid length! Please try again.\n")
        Main()


if __name__ == "__main__":
    genPass = Main()
    print("\nGenerated Password:\n" + genPass)
