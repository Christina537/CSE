# Christina Estrada


import random


money = 15
played = 0




while money > 0:
    dic_1 = (random.randint(1, 6))
    dic_2 = (random.randint(1, 6))
    print("dic_1 : %s" % dic_1)
    print("dic_2 : %s" % dic_2)
    played += 1

    roll = (dic_1 + dic_2)
    if roll == 7:
        money += 4
    elif roll != 7:
        money -= 1

if money == 0:
    print("you played %s rounds" % played)







