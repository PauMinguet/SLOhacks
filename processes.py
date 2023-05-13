

def sign_in():
    print()

    while True:
        user_name = input("New Username: ")
        if sortNames.find(user_name):
            print("Username already in use\nPlease try again")
        else:
            break

    sortNames.insert(user_name)

    password = input("New Password: ")

    userFile = user_name + ".txt"
    with open(userFile, "w") as f:
        f.write(user_name + "\n")
        f.write(password)


def log_in():
    user_name = input("Username: ")
    while True:
        try:
            with open(user_name + ".txt", "r") as f:
                lines = f.readlines(2)
                password = lines[1].strip()
            break
        except:
            print("Incorrect username.\nPlease try again")

    
    while True:
        attempt = input("Password: ")
        if attempt != password:
            print("Incorrect password.\nPlease try again")
        else:
            break