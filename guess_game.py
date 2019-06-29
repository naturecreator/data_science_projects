# The game continues untill the guess is matched, while keeping track of number of guesses at the end of the game or user enters "exit"

import random

number = random.randint(1,9)
guess = 0
count = 0

while guess!=number and guess!="exit":
    guess = input("What's your guess?")
    
    if guess=="exit":
        break
        
    guess=int(guess)
    count +=1
    
    if guess < number:
        print("Guessed number is too low")
    elif guess > number:
        print("Guessed number is too high")
    else:
        print("Your guess is right")
        print("Number of tries took are",count)
 
