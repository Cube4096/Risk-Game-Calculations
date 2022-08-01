#1 vs 1
a1vsd1 = [0,0]

for at1 in range(6):
    for def1 in range(6):
        if at1 > def1:
            a1vsd1[0] += 1
        else:
            a1vsd1[1] += 1


#2 vs 1
a2vsd1 = [0,0]

for at1 in range(6):
    for at2 in range(6):
        for def1 in range(6):
            if at1 > def1 or at2 > def1:
                a2vsd1[0] += 1
            else:
                a2vsd1[1] += 1


#3 vs 1
a3vsd1 = [0,0]

for at1 in range(6):
    for at2 in range(6):
        for at3 in range(6):
            for def1 in range(6):
                if at1 > def1 or at2 > def1 or at3 > def1:
                    a3vsd1[0] += 1
                else:
                    a3vsd1[1] += 1


#1 vs 2
a1vsd2 = [0,0]

for at1 in range(6):
    for def1 in range(6):
        for def2 in range(6):
            #Attack 1 vs 1
            if at1 > def1 and at1 > def2:
                a1vsd2[0] += 1
            else:
                a1vsd2[1] += 1


#2 vs 2
a2vsd2 = [0,0,0]

for at1 in range(6):
    for at2 in range(6):
        for def1 in range(6):
            for def2 in range(6):

                defenderslost = 0
                attackerslost = 0
                attackdice = [at1,at2]
                defenddice = [def1,def2]
                attackdice.sort()
                defenddice.sort()
                if attackdice[1] > defenddice[1]:
                    defenderslost += 1
                else:
                    attackerslost += 1
                if attackdice[0] > defenddice[0]:
                    defenderslost += 1
                else:
                    attackerslost += 1

                if attackerslost == 0:
                    a2vsd2[0] += 1
                if attackerslost == 1:
                    a2vsd2[2] += 1
                if attackerslost == 2:
                    a2vsd2[1] += 1


#3 vs 2
a3vsd2 = [0, 0, 0]

for at1 in range(6):
    for at2 in range(6):
        for at3 in range(6):
            for def1 in range(6):
                for def2 in range(6):

                    defenderslost = 0
                    attackerslost = 0
                    attackdice = [at1, at2, at3]
                    defenddice = [def1, def2]
                    attackdice.sort()
                    defenddice.sort()
                    if attackdice[2] > defenddice[1]:
                        defenderslost += 1
                    else:
                        attackerslost += 1
                    if attackdice[1] > defenddice[0]:
                        defenderslost += 1
                    else:
                        attackerslost += 1

                    if attackerslost == 0:
                        a3vsd2[0] += 1
                    if attackerslost == 1:
                        a3vsd2[2] += 1
                    if attackerslost == 2:
                        a3vsd2[1] += 1

print(str(a1vsd1[0]/sum(a1vsd1))+ " " + str(a1vsd1[1]/sum(a1vsd1)))
print(str(a2vsd1[0]/sum(a2vsd1))+ " " + str(a2vsd1[1]/sum(a2vsd1)))
print(str(a3vsd1[0]/sum(a3vsd1))+ " " + str(a3vsd1[1]/sum(a3vsd1)))

print(str(a1vsd2[0]/sum(a1vsd2))+ " " + str(a1vsd2[1]/sum(a1vsd2)))
print(str(a2vsd2[0]/sum(a2vsd2))+ " " + str(a2vsd2[1]/sum(a2vsd2))+ " " +str(a2vsd2[2]/sum(a2vsd2)))
print(str(a3vsd2[0]/sum(a3vsd2))+ " " + str(a3vsd2[1]/sum(a3vsd2))+ " " +str(a3vsd2[2]/sum(a3vsd2)))
