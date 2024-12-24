import random
random_int=0

def gen_number():
    global random_int
    random_int=random.randint(1,50)
    #print(random_int)
    return  random_int



