# Christina Estrada


import random


money = 15
played = 0
highest = money
broke = False
total_rounds = 0


while money > 0:
    dic_1 = (random.randint(1, 7))
    dic_2 = (random.randint(1, 7))
    print("dic_1 : %s" % dic_1)
    print("dic_2 : %s" % dic_2)
    played += 1

    roll = (dic_1 + dic_2)
    if roll == 7:
        money += 4
        if money > highest:
            highest = money
            total_rounds = played
    elif roll != 7:
        money -= 1
        played += 1

if money == 0:
    print("you played %s rounds" % played)
    if highest < 15:
        print("you didn't earn any money ")
    elif highest > 14:
        print("You should've stopped at round %s when you had $%s" % (total_rounds, highest))
        broke = True







