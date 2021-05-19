import time

users = {}
status = ""


def main_menu():
    global status
    status = input("Do you have a login account? y/n? or press q to quit: ")
    if status == "Y" or status == "y":
        return old_user()
        # break
    elif status == "N" or status == "n":
        return new_user()
        # break
    elif status == "q" or status == "Q":
        quit()


def new_user():
    create_login = input("Create a login name: ")
    if create_login in users:
        print("\nThis login already exists, try another")
    else:
        create_pass = input("Create a password: ")
        users[create_login] = create_pass
        print("\nNew user created!\n")
        logins = open("C:/Users/aader/Repos/biblequiz/logins.txt", "a")
        logins.write("\n" + create_login + " " + create_pass)
        logins.close()


def old_user():
    login = input("Enter your login name: ")
    password = input("Enter your password: ")
    if login in users and users[login] == password:
        print("\nLogin successful")
        print("User:", login, "accessed the system on:", time.asctime())
    else:
        print("\nUser does not exist, or wrong password provided")


main_menu()
