# 12.4.17
def reverse_order(first_name, last_name):
    # print("%s %s" % (last_name, first_name))
    print(last_name + " " + first_name) # Concatenation

    reverse_order("Mr.", "Wiebe")

def reverse_order():
    first_name = input('What is your first name?')
    last_name = input('What is your last name?')
    print("%s %s" % (last_name, first_name))

"""Warmup #2
Write a function called "happy_bday"
that "sings" (prints)
the Happy Birthday

It must take one parameter called "name"
"""


def happy_bday(name):
    print("Happy birthday to you,")
    print("Happy birthday to you,")
    print("Happy birthday dear %s" % name)
    print("Happy birthday to you!")


# 12.5.17
def add_py(name):
    print("%s.py" % name) # Solution 1
    print(name + ".py") # Solution 2

# 12.6.17
def add(num1, num2, num3):
    print(num1 + num2 + num3)

    add(90, 900, 9000)
    add()
