#Author: Leala Laukkonen
#Date: September 16, 2026
import random                                             #import needed
secret_number=random.randint(1,100)                 #random number assignment

print("Step right up and play 'The Magical Number Guessing Game'!")
print("I'm thinking of a number between 1 and 100. What is it?")
print("If you take too long, the number might slip my mind and I'll have to pick a new one!")

while True:
    for guess in range(1,6):                                #"5 guesses before the number changes"
        guess = int(input("You guess: "))                   #integer transform just in case
        if guess == secret_number:                          #correct answer
            print("You Won! Congratulations!")
            break                                           #break from 'for' loop
        elif guess > secret_number:                         #overshoot hint
            print("Too high.")
        elif guess < secret_number:                         #undershoot hint
            print("Too low.")
    answer=input("*yawn* Too long, do you want to try your luck again? (y/n): ")
    if answer=="y":
        secret_number=random.randint(1,100)           #redo/new random number assignment
        continue                                            #repeat: back to top of loop
    else:
        break                                               #end: break from 'while True' loop

print("The secret number was...")                           #answer reveal
print(secret_number)
print("Thanks for playing! Come back soon!")