import time


users = {}
status = ""


def mainMenu():
    global status
    status = input("Do you have a login account? y/n? or press q to quit: ")
    if status == "Y" or status == "y":
        oldUser()
        #break          
    elif status == "N" or status == "n":
        newUser()
        #break           
    elif status == "q" or status == "Q":
        quit()
   

def newUser():
    createLogin = input("Create a login name: ")
    if createLogin in users:
        print("\nThis login already exists, try another")
    else:
        createPass = input("Create a password: ")
        users[createLogin] = createPass
        print("\nNew user created!\n")
        logins = open("C:/Users/aader/Repos/biblequiz/logins.txt", "a")
        logins.write("\n"+createLogin +" " + createPass)
        logins.close()
        
    
       
       

def oldUser():
    login = input("Enter your login name: ")
    password = input("Enter your password: ")
    if login in users and users[login] == password:
        print("\nLogin successful")
        print("User:", login, "accessed the system on:", time.asctime())
    else:
        print("\nUser does not exist, or wrong password provided")


while status != "q" or status != "Q":
    status = mainMenu()

