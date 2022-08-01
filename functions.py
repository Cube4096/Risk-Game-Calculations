import database

try:
    datab = database.data
except:
    datab = {}

ACCEPT = 3
DELETE = 2
PASS = 1

ATTACKMATRIX = [[[0.4167, 0.5833], [0.2546, 0.7454]],
                [[0.5787, 0.4213], [0.2276, 0.4483, 0.3241]],
                [[0.6597, 0.3403], [0.3717, 0.2926, 0.3358]]]

def examine(partial_solution):
    if partial_solution[0] == 0:
        return ACCEPT
    if partial_solution[1] == [0]*len(partial_solution[1]):
        return ACCEPT
    return PASS

def extend(partial_solution):
    attackers = partial_solution[0]
    conquered_squares = 0
    for i in partial_solution[1]:
        if i == 0:
            conquered_squares += 1

    defenders = partial_solution[1][conquered_squares]

    if (attackers, defenders) in datab:
        return_list = []
        for key in datab[(attackers, defenders)]:
            conquer_penalty = 0
            defenderlist = [0] * conquered_squares
            defenderlist.append(key[1])
            for unused_defenders in partial_solution[1][(conquered_squares+1):]:
                defenderlist.append(unused_defenders)
            if key[1] == 0:
                conquer_penalty = -1
            return_list.append([key[0] + conquer_penalty, defenderlist.copy(), datab[(attackers, defenders)][key] * partial_solution[2]])
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

    defenderlist1 = [0] * conquered_squares
    defenderlist2 = [0] * conquered_squares
    defenderlist3 = [0] * conquered_squares

    if attackers >= 2 and defenders >= 2:
        defenderlist1.append(0 + spare_defenders)
        for unused_defenders in partial_solution[1][(conquered_squares + 1):]:
            defenderlist1.append(unused_defenders)

        defenderlist2.append(2 + spare_defenders)
        for unused_defenders in partial_solution[1][(conquered_squares + 1):]:
            defenderlist2.append(unused_defenders)

        defenderlist3.append(1 + spare_defenders)
        for unused_defenders in partial_solution[1][(conquered_squares + 1):]:
            defenderlist3.append(unused_defenders)

        conquer_penalty = 0
        if spare_defenders == 0:
            conquer_penalty = -1

        return [[attackers + spare_attackers + conquer_penalty,
                 defenderlist1, ATTACKMATRIX[attackers - 1][defenders - 1][0] * partial_solution[2]],
                [attackers - 2 + spare_attackers,
                 defenderlist2, ATTACKMATRIX[attackers - 1][defenders - 1][1] * partial_solution[2]],
                [(attackers - 1) + spare_attackers,
                 defenderlist3, ATTACKMATRIX[attackers - 1][defenders - 1][2] * partial_solution[2]]]

    else:
        conquer_penalty = 0
        if defenders == 1:
            conquer_penalty = -1
        defenderlist1.append((defenders - 1) + spare_defenders)
        for unused_defenders in partial_solution[1][(conquered_squares + 1):]:
            defenderlist1.append(unused_defenders)

        defenderlist2.append(defenders + spare_defenders)
        for unused_defenders in partial_solution[1][(conquered_squares + 1):]:
            defenderlist2.append(unused_defenders)

        return [[attackers + spare_attackers + conquer_penalty,
                 defenderlist1,
                 ATTACKMATRIX[attackers - 1][defenders - 1][0] * partial_solution[2]],
                [(attackers - 1) + spare_attackers,
                 defenderlist2, ATTACKMATRIX[attackers - 1][defenders - 1][1] * partial_solution[2]]]

def solve(partial_solution):
    exam = examine(partial_solution)
    if exam == ACCEPT:
        return [partial_solution]
    elif exam != DELETE:
        solutions = []
        for p in extend(partial_solution):
            rec_sols = solve(p)
            solutions.extend(rec_sols)
        return solutions

def verwerkt_sol(attackers, defenders, chance=1):
    situation = [attackers, defenders, chance]
    solution = solve(situation)
    for sub_sol in solution:
        if sub_sol[1] == [0] * len(sub_sol[1]):
            sub_sol[0] += 1
    dic_sol = merge_sol(solution)
    return dic_sol

def sort_and_count_int(solutions, count_pos):
    tot_kans = 0
    for key in solutions:
        if key[count_pos] != 0:
            tot_kans += solutions[key]
    return tot_kans

def sort_and_count_tuple(solutions, count_pos, group):
    tot_kans = 0
    for key in solutions:
        if key[count_pos][group] != 0:
            tot_kans += solutions[key]
    return tot_kans

def attackers_win(solutions):
    att_wins_prosc = sort_and_count_int(solutions, 0)
    return att_wins_prosc

def defenders_win(solution):
    winnerlist = [0] * len(next(iter(solution))[1])
    for winner_index in range(len(winnerlist)):
        winnerlist[winner_index] = sort_and_count_tuple(solution, 1, winner_index)

    return winnerlist

def merge_sol(solutions):
    Dict = dict()
    for i in solutions:
        procent_chance = i[2]
        x = i[0]
        y = tuple(i[1])
        if not (x, y) in Dict:
            Dict[(x, y)] = 0
        if (x, y) in Dict:
            Dict[(x, y)] += procent_chance

    return Dict
