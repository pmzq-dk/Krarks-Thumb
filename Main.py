import random

def Coin():
    if random.randint(0,1) == 1:
        print(True)
        return True
    else:
        print(False)
        return False

def Flip(krark):
    if krark == True:
        print("Krark on")
        if Coin() == False:
            if Coin() == False:
                return False
            else:
                return True
        else:
            return True
    else:
        if Coin() == True:
            return True
        else: 
            return False
        
def FlipX(krark, x):
    win = 0
    lose = 0
    for i2 in range(x):
        if Flip(krark) == True:
            win += 1
        else:
            lose += 1
    print("Won:", win, "Lose:", lose)
    return

def FlipTF(krark):
    win = 0
    while True:
        if Flip(krark) == True:
            win += 1
        else:
            print("Won:", win, "times")
            return


krark = False


while True:
    temp = int(input("""1 - Flip once
2 - Flip x Times
3 - Flip till Fail
4 - krark ON/OFF
:"""))
    if temp == 1:
        if Flip(krark) == True:
            print("Won Flip")
        else: 
            print("Lost Flip")
    elif temp == 2:
        x = int(input("How many flips: "))
        FlipX(krark, x)
    elif temp == 3:
        FlipTF(krark)
    elif temp == 4:
        if krark == False:
            print("Krark's Thumb on")
            krark = True
        else:
            print("Krark's Thumb off")
            krark = False
    print("")
    

    