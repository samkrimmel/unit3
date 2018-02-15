#Sam Krimmel
2/15/18
#numberGuessingGame.py - guess the number!
from random import randint

num = randint(1,100)

while True:
    guess = int(input('Guess a number! '))
    if guess == num:
        print('You guessed it!')
    elif guess > num:
        print('Too high!')
    else:
        print('Too low!')
    

