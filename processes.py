import sortNames


def process(user_name):
    while True:
        var = input(
            """
        What do you want to do?
            - Want to add friends? Press 'a'
            - Want to see who you owe money? Press 'l'
            - Want to pay the debt? Press 'p'
            - Want to change the amount owed? Press 'n'   NOTE : ADD THIRD AMOUNT TO KEEP TRACK OF MONEY OWED BY OTHERS
            - Exit (e)
        """
        )
        if var == "e":
            break
        elif var == "a":
            addfriend(user_name)
        elif var == "l":
            user_data = get_user_data(user_name)
            listfriends(user_data)
        elif var == "p":
            receiver = input("Who would you like to pay?")
            amount = input("How much would you like to pay?")
            payFriend(user_name, receiver, amount)
        elif var == "n":
            receiver = input("Who's debt are you trying to update?")
            amount = input("What would you like to change it to?")
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
        f.write(password)
    process(user_name)


def log_in(user_name, password):
    try:
        with open("users.txt", "r"):
            pass
    except:
        with open("users.txt", "x"):
            pass
    while True:
        if not sortNames.find(user_name):
            print("Incorrect username.\nPlease try again")
        else:
            break

    with open(user_name + ".txt", "r") as f:
        lines = f.readlines()
        print(lines)
        savedPassword = lines[1].strip()

    while True:
        if password != savedPassword:
            print("Incorrect password.\nPlease try again")
        else:
            break

    process(user_name)


def addfriend(user_name):
    while True:
        attempt = input("Search: ")
        if not sortNames.find(attempt):
            print("This user does not exist.\nPlease try again")
            break
        else:
            break

    print("You have added " + attempt + ".")

    with open(user_name + ".txt", "w") as f:
        f.write(attempt + " 0\n")

    with open(attempt + ".txt", "w") as f:
        f.write(user_name + " 0\n")


def get_user_data(user_name):
    with open(user_name + ".txt", "r") as f:
        lines = f.readlines()
        print()
        print("Welcome, " + lines[0].strip())
    return lines


def listfriends(user_data):
    friends = user_data[2:]
    for friend in friends:
        print(friend.strip().split()[0] + " " + friend.strip().split()[1])


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
                print("yes")
                if amount <= buddyOwe:
                    buddyOwe -= amount
                    print(buddyOwe)
                buddy = buddyName + " " + str(buddyOwe)
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
                buddyOwe = amount
                buddy = buddyName + " " + str(buddyOwe)
            f.write(buddy)
