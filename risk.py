from functions import verwerkt_sol, defenders_win
from databasemaker import create_db

atac = int(input("Attackers:"))

defe = []
counter = 1
defeinput = int(input("Defenders (pos: " + str(counter)+"):"))
while defeinput != -1:
    counter += 1
    defe.append(defeinput)
    defeinput = int(input("Defenders (pos: " + str(counter) + "), (or enter -1 to finish):"))

if not defe:
    raise Warning("No defenders, unvalid attack")

print("Defenders (total): ", end="")
print(str(defe[0]), end="")
for i in range(len(defe)-1):
    print(", " + str(defe[i+1]), end="")
print("")
print("Attackers (total): " + str(atac))

solution = verwerkt_sol(atac, defe)

Spellingsdict = {1: "first", 2: "second", 3: "third", 4: "fourth", 5: "fifth", 6: "sixth", 7: "seventh", 8: "eight"}

outcomes = defenders_win(solution)
for def_win_index in range(len(outcomes)):
    print("Chance ", end="")
    if (def_win_index + 1) in Spellingsdict:
        print(Spellingsdict[def_win_index + 1], end="")
    else:
        print(def_win_index+1, end="")
    print(" attack succeeds: " + str(1 - round(outcomes[def_win_index], 3)))
