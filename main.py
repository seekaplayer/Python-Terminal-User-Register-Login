def question(value):
    answer = input(value)
    return answer.lower()


def data_match_conf(val1, val2):
    if val1 == val2:
        return True


def user_data(value, var):
    answer = input(value)
    while answer == "":
        answer = input(f"the {var} field is required ")
    return answer


# welcome the user when the program starts
print("Hello Welcome to the User Register/Login System")
quest_start = question("Would you like to Login or Register? ")

while quest_start != "register" and quest_start != "login":
    quest_start = question("You have to make a choice to either Register or Login ")

if quest_start == "register":
    print("Great! Let's get you signed up!")
    username = user_data("Choose a username: ", "Username")
    email = user_data("What is your email? ", "Email")
    password = user_data("choose a password: ", "Password")
    password2 = user_data("Confirm Password: ", "Password Confirmation")
    print("Congrats!")

    while password == "":
        password = input("You need to choose a password")

elif quest_start == "login":
    print("great let's login ")
