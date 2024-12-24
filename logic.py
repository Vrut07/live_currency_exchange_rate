import game.user_input as user_input 
import game.number_genetration as a
import game.levels as b

b.definng_levels()

def input2():
    if(b.attempts==0):
        print("BUT OH NO! YOUR ATTEMPTS ARE OVER.")
        retry=input("DO YOU WANT TO RETRY IT?? (yes or no) :")
        if(retry=='yes'):
            print("s")
            b.definng_levels()
        elif(retry=='no'):
            print("\nTHANK YOU FOR PLAYING THIS GAME.")
        else:
            print("please enter a valid input.")
    else:
        user_input.user_number=int(input(f"ITS OKAY YOU HAVE {b.attempts} ATTEMPTS LEFT\nGUESS ANOTHER NUMBER :"))


def program_logic():
    while(b.attempts>0):
        if (user_input.user_number<a.random_int and user_input.user_number<=50):
            b.attempts=b.attempts-1
            print("\nYOU HAVE ENTERED LESS THAN YOUR LUCKY NUMBER.")
            input2()
            program_logic()

        elif (user_input.user_number>a.random_int and user_input.user_number<=50):
            b.attempts=b.attempts-1
            print("YOU HAVE ENTERED MORE THAN YOUR LUCKY NUMBER.")
            input2()
            program_logic()

        elif(user_input.user_number==a.random_int):
            print("Congratulation... YOU FOUND GOT THE LUCKY NUMBER.")
            b.attempts=0
        else:
            print("ENTER A VALID NUMBER")
            print("NOW YOU HAVE RESTART THE GAME.")
            b.attempts=0
            
    
    





 
