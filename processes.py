import sortNames


def process(user_name):
    while True:
        var = input(
            """
        What do you want to do?
            - Add friends (a)
            - List your debts (l)
            - Pay (p)
            - New debt (n)
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


def sign_in(user_name, password):
    while True:
        # user_name = input("New Username: ")
        if sortNames.find(user_name):
            print("Username already in use\nPlease try again")
        else:
            break

    sortNames.insert(user_name)

    # password = input("New Password: ")

    userFile = user_name + ".txt"
    with open(userFile, "w") as f:
        f.write(user_name + "\n")
        f.write(password)
    process(user_name)


def log_in(user_name, password):
    while True:
        # user_name = input("Username: ")
        if not sortNames.find(user_name):
            print("Incorrect username.\nPlease try again")
        else:
            break

    with open(user_name + ".txt", "r") as f:
        lines = f.readlines()
        savedPassword = lines[1].strip()

    while True:
        # attempt = input("Password: ")
        if password != savedPassword:
            print("Incorrect password.\nPlease try again")
        else:
            break
    #return user_name
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

    with open(user_name + ".txt", "a") as f:
        f.write(attempt + " 0\n")

    with open(attempt + ".txt", "a") as f:
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
