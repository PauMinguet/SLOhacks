import sortNames
import processes

with open("users.txt","r"):
    pass
print("=====  OWING MONEY APP  =====")
print()
var = input("Log in or sign up (l or s)? ")

if var == "s":
    sign_in()



elif var == "l":

    log_in()

    UserAccount.main()
    

    with open(user_name + ".txt", "r") as f:
            lines = f.readlines()
            print()
            print("Welcome, " + lines[0].strip())
            friends = lines[2:]

            for friend in friends:
                print(friend.strip().split()[0])


    var = input(
        """
        What do you want to do?
            - Add friends (a)
            - List your debts (l)
            - Pay a debt (p)
            - Exit (e)
        """
    )

    while var != 'e':
        if var == "a":
            
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
