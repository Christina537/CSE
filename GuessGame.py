# Christina Estrada


import random
number = (random.randint(1, 50))
guess = ""
print(number)
guesses_made = 0

while guess != number and guesses_made < 5:
    guess = int(input("What number am i thinking from 1-50? "))
    guesses_made += 1
    if guess > number:
        print("Lower")
    elif guess < number:
        print("Higher")
    else:
        print("You got it!")




