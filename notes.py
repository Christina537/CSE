print("Hello World!")

# Christina

print(3 + 5)
print(5 - 3)
print(5 * 3)
print(6 / 2)
print(3 ** 2)

print()
print("See if you can figure this out")
print(15 % 5)

# Variables
car_name = "Dragon Beauty"
car_type = "Volkswagen Van"
car_cylinders = 8
car_mpg = 9000.1

# Inline Printing
print("My car is the %s." % car_name)
print("My car is the %s. It is a %s" % (car_name, car_type))

# Taking input
name = input("What is your name?")
print("Hello %s." % name)
# print(name)
age = input("What is your age?")
print("I'm also %s." % age)


def print_hw():
    print("Hello World")


print_hw()


def say_hi(name):  # name is a "parameter"
    print("Hello %s." % name)
    print("I hope you have a fantastic day.")


say_hi("John")


def birthday(age):
    age += 1  # age = age + 1
    print(age)


say_hi("John")
print("John is 15. Next year:")
birthday(15)
#
# Press Ctrl-A and Ctrl-/
# to comment old code


def f(x):
    return x**5 + 4 * x ** 4 - 17*x**2 + 4


print(f(3))
print(f(3) + f(5))

# If statements


def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:  # Else if
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"

grade_calc(78)
# Loops


for num in range(10):
    print(num + 1)

for mystery in "Hello World":
    print(mystery)

a = 1
while a < 10:
    print(a)
    a += 1

response = ""
# while response != "Hello":
#     response = input("Say \"Hello\"")

print("Hello \nWorld")  # \n means newline

import random  #imports should be at the top
print(random.randint(0, 6))

# Comparisons
print(1 == 1) # Two equal signs to compare
print(1 != 2) # One is not equal to 2
print(not False) # This prints True
print(1 == 1 and 4<=5)
print(1 < 0 or 5 > 1)




# Recasting
c = '1'
print(c == 1) # False - C is a string, 1 is an int
print(int(c) == 1) # True - Compares two ints
print(c == str(1)) # True - Compares two strings


num = input("Give me a number")
# Inputs are ALWAYS (!!!!!!!) of type of string!!!