import re
import getpass
import json

# function that checks if they want to register or login
def reg_or_log(value):
    answer = input(value).lower()
    # runs a while loop to check to make sure they answered with register or login
    while answer != "register" and answer != "login":
        answer = input("You have to make a choice to either Register or Login ").lower()
    return answer


def user_data(value, var):
    answer = input(value)
    while answer == "":
        answer = input(f"the {var} field is required ")
    return answer


def validate_email(value):
    regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    while not re.search(regex, value):
        value = input("Invalid Email Format, Try Again: ")
    return value


def password_input(value, var):
    print(value)
    answer = getpass.getpass()
    while answer == "":
        print(f"the {var} field is required ")
        answer = getpass.getpass()
    return answer


def password_match(val1, val2):
    while val2 != val1:
        print("Passwords don't match!")
        val2 = getpass.getpass()
    return val2


def register():
    print("Great! Let's get you signed up!")
    username = user_data("Choose a username: ", "Username")
    email = user_data("What is your email? ", "Email")
    email = validate_email(email)
    password = password_input("choose a password: ", "Password")
    password2 = password_input("Confirm Password: ", "Password Confirmation")
    password_match(password, password2)
    password = password2
    print("You're Registered, Please Login")
    start_program()


def login():
    print("great let's login ")


def start_program():
    # welcomes the user to the program
    print("Hello Welcome to the User Register/Login System")
    # calls the question function
    user_path = reg_or_log("Would you like to Login or Register? ")
    # if the user chose to register then they go to that stage of the app
    if user_path == "register":
        register()
    # if the user chose to login then they go to that stage of the app
    elif user_path == "login":
        login()


start_program()