# Christina Estrada


import random
number = (random.randint(1, 50))
guess = ""
print(number)
guesses_made = 0

while guess != number and guesses_made < 5:
    guess = int(input("What number am i thinking from 1-50? "))

    if guess > number:
        guesses_made += 1
        print("Lower")
    elif guess < number:
        guesses_made += 1
        print("Higher")
    else:
        print("You got it!")
if guesses_made >= 5:
  print("Better luck next time")




