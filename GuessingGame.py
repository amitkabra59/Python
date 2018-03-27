import random
guessTaken=0
print("What is ur name?")
name=raw_input()
print('Well, '+name +', I am thinking of a number from 1 to 20')
randomNumber=random.randint(1,20)

while guessTaken<6:
    guess=raw_input('TAKE A GUESS \n')
    guess=int(guess)
    guessTaken+=1

    if randomNumber<guess:
        print('You\'re too high')
    elif randomNumber>guess:
        print('You\'re too low')
    else:
        break
    
    
if guess==randomNumber:
    guess=str(guess)
    guessTaken=str(guessTaken)
    print('You won '+name+'. You guessed number in '+guessTaken +' guesses' )

if guessTaken==6:
    randomNumber=str(randomNumber)
    print('Nope. The number I was thinking of is '+randomNumber)
    
    
