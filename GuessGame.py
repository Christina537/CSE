# Christina Estrada


import random
number = (random.randint(1,50))
guess = ""
print(number)

while guess != number:
    guess = input("What number am i thinking from 1-50?")
    if (int(guess)> number:
        print("Lower")
    if guess < number:
        print("Higher")



