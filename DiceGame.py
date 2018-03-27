import random
info = '''
    Which sided dice would you like to roll? You can choose a
    4-sided dice, a 6-sided dice or a 12-sided dice.
    (Type 0 to exit the loop)
    '''
print(info)
while True:
        dice = random.randrange(1,5)
        dice2 = random.randrange(1,7)
        dice3 = random.randrange(1,13)
        sides = int(input("Input number 4, 6 or 12 > "))
        if sides == 0:
            break  # exit the endless while loop
        elif sides == 4 :
            print("The 4-sided dice has rolled to", dice)
        elif sides == 6 :
            print("The 6-sided dice has rolled to", dice2)
        elif sides == 12:
            print("The 12-sided dice has rolled to", dice3)
        else:
            print("Please input a number 4, 6 or 12")
