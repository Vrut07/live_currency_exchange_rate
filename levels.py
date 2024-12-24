def definng_levels():
    global attempts
    lvl=input("=>HELLO GAMER'Z , WELCOME TO THIS GAME. \n=>THIS GAME IS ABOUT GUESSING YOUR LUCKY NUMBER. \n\n=>CHOOSE DIFFICULTY LEVEL (EASY(10 Ampt) OR HARD(4 Ampt)) :")
    if(lvl=='easy' or lvl=='EASY'):
        attempts=9
        return attempts
    elif(lvl=='hard' or lvl=='HARD'):
        attempts=4
    else:
        print("Please write proper input.")
        definng_levels()
        return attempts
    
