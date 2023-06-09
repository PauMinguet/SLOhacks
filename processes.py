import sortNames
import main


def process(user_name):
    print("\nWelcome, " + user_name)
    while True:
        var = input(
            """
    MAIN MENU
    - Want to add friends? Press 'a'
    - Want to see who you owe money? Press 'l'
    - Want to pay a debt? Press 'p'
    - Want to create a new debt? Press 'n'
    - Log out (o)
    - Exit (e)          """
        )
        if var == "e":
            break
        elif var == "o":
            main.main()
        elif var == "a":
            addfriend(user_name)
        elif var == "l":
            user_data = get_user_data(user_name)
            listfriends(user_data)
        elif var == "p":
            receiver = input("Who would you like to pay? ")
            amount = input("How much would you like to pay? ")
            payFriend(user_name, receiver, amount)
        elif var == "n":
            receiver = input("Who's debt are you trying to update? ")
            y_n = input("Do you owe them money? (y/n) ")
            amount = input("How much money? ")
            if y_n == "y":
                amount = "-" + amount
            newDebt(user_name, receiver, amount)


def sign_in():
    try:
        with open("users.txt", "r"):
            pass
    except:
        with open("users.txt", "x"):
            pass
    print()
    while True:
        user_name = input("Please enter your username : ")
        if sortNames.find(user_name):
            print("This username is already in use\nPlease try again")
        else:
            break
    password = input("Enter Password : ")

    sortNames.insert(user_name)

    userFile = user_name + ".txt"
    with open(userFile, "w") as f:
        f.write(user_name + "\n")
        f.write(password + "\n")
    process(user_name)


def log_in():
    try:
        with open("users.txt", "r"):
            pass
    except:
        with open("users.txt", "x"):
            pass
    while True:
        user_name = input("Please enter your username : ")
        if not sortNames.find(user_name):
            print("Incorrect username.\nPlease try again")
        else:
            break

    with open(user_name + ".txt", "r") as f:
        lines = f.readlines()
        savedPassword = lines[1].strip()

    while True:
        password = input("Password : ")
        if password != savedPassword:
            print("Incorrect password.\nPlease try again")
        else:
            break
    process(user_name)


def addfriend(user_name):
    while True:
        attempt = input("What is your friend's name : ")
        if not sortNames.find(attempt):
            print("This user does not exist.\nPlease try again")
        else:
            with open(user_name + ".txt", "a") as f:
                f.write(attempt + " 0\n")

            with open(attempt + ".txt", "a") as f:
                f.write(user_name + " 0\n")
            print("You have added " + attempt + ".")
            break
    print("Friend successfully added!")


def get_user_data(user_name):
    with open(user_name + ".txt", "r") as f:
        lines = f.readlines()
    return lines


def listfriends(user_data):
    i_owe = []
    they_owe = []
    zero = []

    friends = user_data[2:]
    for friend in friends:
        if int(friend.strip().split()[1]) < 0:
            i_owe.append(friend)
        elif int(friend.strip().split()[1]) > 0:
            they_owe.append(friend)
        else:
            zero.append(friend)

    print()
    print("You owe: ")
    for friend in i_owe:
        print(friend.strip().split()[0] + ": " + friend.strip().split()[1][1:] + "$")
    print()
    print("They owe you: ")
    for friend in they_owe:
        print(friend.strip().split()[0] + ": " + friend.strip().split()[1] + "$")
    print()
    print("In peace: ")
    for friend in zero:
        print(friend.strip().split()[0] + ": " + friend.strip().split()[1] + "$")
    print()


def payFriend(user_name, friend, amount):
    with open(user_name + ".txt", "r") as f:
        friendList = f.readlines()

    with open(user_name + ".txt", "w") as f:
        f.write(friendList[0])
        f.write(friendList[1])
        for buddy in friendList[2:]:
            buddyName = buddy.split()[0]
            buddyOwe = buddy.split()[1]
            buddyOwe = int(buddyOwe)
            if buddyName == friend:
                buddyOwe += int(amount)
                buddy = buddyName + " " + str(buddyOwe) + "\n"
            f.write(buddy)

    with open(friend + ".txt", "r") as f:
        friendList = f.readlines()

    with open(friend + ".txt", "w") as f:
        f.write(friendList[0])
        f.write(friendList[1])
        for buddy in friendList[2:]:
            buddyName = buddy.split()[0]
            buddyOwe = buddy.split()[1]
            buddyOwe = int(buddyOwe)
            if buddyName == user_name:
                buddyOwe -= int(amount)
                buddy = buddyName + " " + str(buddyOwe) + "\n"
            f.write(buddy)

    



def newDebt(user_name, friend, amount):
    with open(user_name + ".txt", "r") as f:
        friendList = f.readlines()

    with open(user_name + ".txt", "w") as f:
        f.write(friendList[0])
        f.write(friendList[1])
        for buddy in friendList[2:]:
            buddyName = buddy.split()[0]
            buddyOwe = buddy.split()[1]
            buddyOwe = int(buddyOwe)
            if buddyName == friend:
                buddyOwe += int(amount)
                buddy = buddyName + " " + str(buddyOwe) + "\n"
            f.write(buddy)

    with open(friend + ".txt", "r") as f:
        friendList = f.readlines()

    with open(friend + ".txt", "w") as f:
        f.write(friendList[0])
        f.write(friendList[1])
        for buddy in friendList[2:]:
            buddyName = buddy.split()[0]
            buddyOwe = buddy.split()[1]
            buddyOwe = int(buddyOwe)
            if buddyName == user_name:
                buddyOwe -= int(amount)
                buddy = buddyName + " " + str(buddyOwe) + "\n"
            f.write(buddy)
    print("The amount is changed!")
