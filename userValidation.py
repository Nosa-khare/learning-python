from sys import exit
from random import randint
from string import ascii_lowercase


def user_details():
    firstname = input("Type in firstname: ")
    lastname = input("Type in lastname: ")
    email = input("Type in email: ")
    return firstname, lastname, email


def create_password():
    five_characters = []
    alphabets = list(ascii_lowercase)
    for x in range(3):
        five_characters.append(randint(0, 9))
        if len(five_characters) == 5:
            break
        five_characters.append(alphabets[randint(0, 25)])
    # to convert each integer in the list to a string
    five_characters = [str(char) for char in five_characters]
    five_characters = "".join(five_characters)
    key = details[0][:2] + details[1][-2:] + five_characters
    return key


user_data = {}
SN = 1  # User serial number variable

while True:
    details = list(user_details())
    password = create_password()
    print(f"Your password is {password}")
    print("Do you want to create a new password?")

    while True:
        choice = input("Yes/No: ")
        if choice.lower() == "yes":
            password = input("Enter new password (7 characters): ")
            while len(password) < 7:
                print("Password must be at least 7 characters")
                password = input("Enter new password (7 characters): ")
            break
        elif choice.lower() == "no":
            break
        else:
            print("INVALID COMMAND! Type in Yes/No")
    details.append(password)

    user = {
        "Firstname": details[0],
        "Lastname": details[1],
        "Email": details[2],
        "Password": details[3]
    }

    print(f"\nUser {SN} details: {user}\n")
    user_data[f'user {SN}'] = user

    print("Do you want to enter another user?")
    while True:
        add_user = input("Yes/No: ")
        if add_user.lower() == "yes":
            print("")  # to print a blank line in the terminal
            SN += 1  # to add 1 to value of serial number variable(SN)
            break
        elif add_user.lower() == "no":
            for user, details in list(user_data.items()):
                print(f"{user} details: {details}")
            exit(0)
        else:
            print("INVALID COMMAND! Type Yes/No")
