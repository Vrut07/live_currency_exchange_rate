import game.levels as v

user_number=0
def user_in():
    global user_number
    print("\n*OKAY WE HAD GENERATED LUCKY NUMBER FOR YOU*")
    user_number=int(input("=>GUESS LUCKY NUMBER BETWEEN 1 TO 50 :"))
    print("here input file")
    return user_number


