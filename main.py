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

    user_name = processes.log_in()


    user_data = processes.get_user_data(user_name)
    

    while var != 'e':

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

        if var == "a":
            processes.addfriend(user_name)

        elif var == "l":
            processes.listfriends(user_data)
        
        elif var == "p":
            processes.pay(user_name, user_data) ?????????
        
        elif var == "n":
            processes.new_charge(user_name, user_data)??????????
