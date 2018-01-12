# Christina Estrada


import random


money = 15
played = 0
highest = money



while money > 0:
    dic_1 = (random.randint(1, 7))
    dic_2 = (random.randint(1, 7))
    print("dic_1 : %s" % dic_1)
    print("dic_2 : %s" % dic_2)
    played += 1

    roll = (dic_1 + dic_2)
    if roll == 7:
        money += 4
        print("Your max is %s" % highest)
    elif roll != 7:
        money -= 1
        played += 1

if money == 0:
    print("you played %s rounds" % played)







