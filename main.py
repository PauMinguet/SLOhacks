import sortNames
import processes

try:
    with open("users.txt","r"):
        pass
except:
    with open("users.txt","x"):
        pass

print("=====  OWING MONEY APP  =====")
print()
var = input("Log in or sign up (l or s)? ")

if var == "s":
    processes.sign_in()



elif var == "l":
    processes.log_in()

    user.main()


    with open(user_name + ".txt", "r") as f:
            lines = f.readlines()
            print()
            print("Welcome, " + lines[0].strip())
            friends = lines[2:]

            for friend in friends:
                print(friend.strip().split()[0])


    

    while var != 'e':

        var = input(
        """
        What do you want to do?
            - Add friends (a)
            - List your debts (l)
            - Pay a debt (p)
            - Exit (e)
        """
        )

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
