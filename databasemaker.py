import database

datab = database.data

ACCEPT = 3
DELETE = 2
PASS = 1

ATTACKMATRIX = [[[0.4167, 0.5833], [0.2546, 0.7454]],
                [[0.5787, 0.4213], [0.2276, 0.4483, 0.3241]],
                [[0.6597, 0.3403], [0.3717, 0.2926, 0.3358]]]

def examinedb(partial_solution):
    if partial_solution[0] == 0 or partial_solution[1] == 0:
        return ACCEPT
    return PASS

def extenddb(partial_solution):
    attackers = partial_solution[0]
    defenders = partial_solution[1]

    if (attackers, defenders) in datab:
        return_list = []
        for key in datab[(attackers, defenders)]:
            return_list.append([key[0], key[1], datab[(attackers, defenders)][key] * partial_solution[2]])
        return return_list

    if defenders > 2:
        spare_defenders = defenders - 2
        defenders = 2
    else:
        spare_defenders = 0

    if attackers > 3:
        spare_attackers = attackers - 3
        attackers = 3
    else:
        spare_attackers = 0

    if attackers >= 2 and defenders >= 2:
        return [[attackers + spare_attackers,
                 0 + spare_defenders, ATTACKMATRIX[attackers - 1][defenders - 1][0] * partial_solution[2]],
                [attackers - 2 + spare_attackers,
                 2 + spare_defenders, ATTACKMATRIX[attackers - 1][defenders - 1][1] * partial_solution[2]],
                [(attackers - 1) + spare_attackers,
                 1 + spare_defenders, ATTACKMATRIX[attackers - 1][defenders - 1][2] * partial_solution[2]]]

    else:
        return [[attackers + spare_attackers,
                 (defenders - 1) + spare_defenders,
                 ATTACKMATRIX[attackers - 1][defenders - 1][0] * partial_solution[2]],
                [(attackers - 1) + spare_attackers,
                 defenders + spare_defenders, ATTACKMATRIX[attackers - 1][defenders - 1][1] * partial_solution[2]]]

def solvedb(partial_solution):
    exam = examinedb(partial_solution)
    if exam == ACCEPT:
        return [partial_solution]
    elif exam != DELETE:
        solutions = []
        for p in extenddb(partial_solution):
            rec_sols = solvedb(p)
            solutions.extend(rec_sols)
        return solutions

def verwerkt_sol(attackers, defenders, chance=1):
    situation = [attackers, defenders, chance]
    solution = solvedb(situation)
    dic_sol = merge_sol(solution)
    return dic_sol

def merge_sol(solutions):
    Dict = dict()
    for i in solutions:
        procent_chance = i[2]
        x = i[0]
        y = i[1]
        if not (x, y) in Dict:
            Dict[(x, y)] = 0
        if (x, y) in Dict:
            Dict[(x, y)] += procent_chance

    return Dict

def create_db(limit,location = "testdb.py" ,steps = 1, makesteps = 5):
    Database = dict()
    datab = Database
    for i in range(limit):
        print("test:" + str(i + 1))
        if (i + 1) % steps == 0:
            for j in range(limit):
                if (j + 1) % steps == 0:
                    solution = verwerkt_sol(i + 1, j + 1)
                    Database[(i + 1, j + 1)] = solution

                if (i + 1) % makesteps == 0:
                    datab = Database

    f = open(location, "w")
    f.write("data = ")
    f.write(str(datab))