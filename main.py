import processes

def main():
    try:
        with open("users.txt", "r"):
            pass
    except:
        with open("users.txt", "x"):
            pass

    print("=====  OWING MONEY APP  =====")
    print()
    var = input("Log in or sign up (l or s)? ")

    if var == "s":
        processes.sign_in()

    elif var == "l":
        user_name = processes.log_in()

if __name__ == "__main__":
    main()