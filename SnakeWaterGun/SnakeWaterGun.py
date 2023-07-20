import random

comp = random.randint(0,2)
user = int(input("Enter your choice 1 for gun, 2 for snake and 0 for water : "))

def check(comp,user):
    if(comp == user):
        return 0
    elif(comp == 0 and user == 1):
        return -1
    elif(comp == 1 and user ==2):
        return -1
    elif(comp == 2 and user == 0):
        return -1
    return 1

print("Computer : ",comp, " User : ",user)
if(check(comp,user) == 0):
    print("It's a draw")
elif(check(comp,user) == -1):
    print("You lose")
else:
    print("You won")
