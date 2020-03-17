import itertools
from collections import deque
from time import perf_counter
from os.path import join
import os

"""
nb echecs -> nb fois que S pas consistant ? 
nb clauses unitaires propagés -> le nombre de clause unitaire qu'on trouve au total ?

"""


def parse_sat(file):
    with open(file) as f:
        L = f.readlines()
        L = [x.strip().split()
             for x in L if not(x.startswith("c") or len(x.strip().split()) <= 1)]
        C = [list(map(int, e[:-1])) for e in L[1:]]
        p, cnf = list(map(int, (L[0][2:])))

    # print(f"p : {p}; cnf : {cnf}")

    return p, C


def parse_graph(file):
    with open(file) as f:
        L = f.readlines()
        L = [x.strip().split()[1:]
             for x in L if not(x.startswith("c") or len(x.strip().split()) <= 1)]
        V = list(map(lambda x: [int(x[0]), int(x[1])], L[1:]))
        edges, vertices = list(map(int, L[0][-2:]))

    # print(f"sommets : {edges} ; arêtes : {vertices} ; V = {V}")
    return edges, vertices, V


# consistant si AUCUN clause fausse (soit tout vrai), donc si UNE FAUSSE -> stop

def keywithmaxval(D):
    return list(D.keys())[list(D.values()).index(max(D.values(), key=lambda x: sum(x)))]


def test_consistance_heurstique1(C, S, p):
    first_missing = None
    clause_uni = None
    flag = False
    flag_cu = False
    CUs = []

    early_stop = 0

    D = {x: (0, 0) for x in range(1, p+1)}

    for c in C:
        clause_size = len(c)
        cpt = 0
        missing = 0
        flag_early_stop = False
        for l in c:  # pour tous les litéraux de la clause
            founded = False
            abs_l = abs(l)
            for X, v, _ in S:  # on cherche leurs valeurs dans S
                if abs_l == abs(X):
                    founded = True
                    if (l > 0 and v > 0) or (l < 0 and v < 0):
                        cpt += 1
                        if not flag_early_stop:
                            early_stop += 1
                            flag_early_stop = True
                        break
            if not founded:
                # print("unfound : ", l)
                old_value = D[abs_l]
                oldt1, oldt2 = old_value
                if l < 0:
                    new_value = (1 + oldt1, oldt2)
                else:
                    new_value = (oldt1, 1 + oldt2)
                D[abs_l] = new_value
                missing += 1
                cu = l
        if missing == 1 and cpt == 0:
            CUs.append(cu)
        if missing == 1 and cpt == 0 and not flag_cu:
            clause_uni = cu
            flag_cu = True

        if cpt == 0 and missing == 0:
            return False, None, None, None

    neg, pos = D[keywithmaxval(D)]
    first_missing = keywithmaxval(D) if pos > neg else keywithmaxval(D)*-1
    # print()
    # print("dico compteurs : ", D)
    # print()
    # print(f"prochaine variable du dico : clé = {first_missing}, valeur = {(neg, pos)} (cpt_neg, cpt_pos)")
    # print()

    lprs = [key for (key, value) in D.items()
            if (value[0] == 0 or value[1] == 0) and (value[0] != value[1])]

    if len(lprs) > 0:
        # print(lprs)
        first_missing = lprs[0]

    # print(D)
    if CUs == []:
        CUs = [None]
    else:
        CUs = list(set(CUs))
        Z = list(map(lambda x: x*-1, CUs))
        Rtemp = set(CUs) - set(Z)
        CUs = Rtemp.union(set([i for i in set(CUs) - Rtemp if i > 0]))

        # print("CUS -> ", CUs)

    if early_stop == len(C):
        return True, 'stop', 'stop', None

    return True, clause_uni, first_missing, CUs


def choisir(S, CU, var_missing, show_print=False):
    global CPT_CU
    if CU != None:  # ajout clause unitaire
        CPT_CU += 1
        return (CU, 1, None) if CU > 0 else (CU*-1, -1, None)
    else:  # ajout var missing
        return (var_missing, 1, -1) if var_missing > 0 else (abs(var_missing), -1, 1)


def backtrack(C, p, fconsist, show_print=False):
    global CPT_FALSE
    begin = perf_counter()
    cpt_aff = 0
    n = p
    fini = False
    S = deque()

    while True:
<<<<<<< HEAD
=======
        if len(S) == p:
            print("Nombre d'itérations finales = ", cpt_aff)
            return S
>>>>>>> 8248dda6a8ed69591c7c43901e5d63c8f261f539
        cpt_aff += 1
        # print(cpt_aff)
        # if cpt_aff % 100 == 0:
        #     print(cpt_aff, len(S), " / ", p, "temps :", perf_counter() % 60)
        TC, CU, var_missing, CUs = fconsist(C, S, p)
        if TC:
            # print(
            #     f"CONSISTANT,\nClauses unitaires = {CUs}\nProchaine variable si pas de CU = {var_missing}")
            if CU == 'stop':
                print(
                    f"INSTANCE SATISFIABLE | Modèle partiel trouvé ({len(S)} sur {p})")
                print("Nombre d'itérations finales = ", cpt_aff)
                return S
            elif len(S) == n:
                print("INSTANCE SATISFIABLE")
                print("Nombre d'itérations finales = ", cpt_aff)
                return S
            else:  # étendre le modèle
                to_append = [choisir(S, cu_i, var_missing) for cu_i in CUs]
                # print(f"On ajoute à S : {to_append}")
                S.extend(to_append)
        else:  # modèle pas consistant
            X, v, vv = S.pop()  # on retire le triplet
            CPT_FALSE += 1
            while len(S) > 0 and vv == None:  # on cherche le prochain avec v' != None
                X, v, vv = S.pop()
            if vv != None:
                S.append((X, vv, None),)
            else:
                print("INSTANCE INSATISFIABLE")
                print("Nombre d'itérations finales = ", cpt_aff)
                return S
        # print("#" * 60, "FIN ITERATION", "#" * 60)
    return S


def main_SAT(p, C):
    begin = perf_counter()
<<<<<<< HEAD

    S = backtrack(C, p, test_consistance_heurstique1)  # compteur de littéraux
    end = perf_counter()
    print(f"CPT ECHECS = {CPT_FALSE}, CPT CLAUSES UNITAIRES PROP. = {CPT_CU}")
    print(f"TEMPS DE CALCUL : {round(end - begin, 2)} secondes")


# p, C = parse_sat("SAT/uf20-01.cnf")
# p, C = parse_sat("SAT/uf50-01.cnf")
# p, C = parse_sat("SAT/uuf50-05.cnf")
# p, C = parse_sat("SAT/uuf125-01.cnf")  # 116895 itérations, 762 secondes
# p, C = parse_sat("SAT/jnh1.cnf")
# p, C = parse_sat("SAT/aim-50-1_6-no-1.cnf")
=======
    # print(p)

    S = backtrack(C, p, test_consistance_heurstique1)  # compteur de littéraux
    end = perf_counter()
    # print(S)
    # print()
    print(f"CPT ECHECS = {CPT_FALSE}, CPT CLAUSES UNITAIRES PROP. = {CPT_CU}")
    print(f"TEMPS DE CALCUL : {round(end - begin, 2)} secondes")
    # print(S)


# p, C = parse_sat("SAT/uuf50-05.cnf")
# p, C = parse_sat("SAT/uf50-01.cnf")
# heuristique 1 : 6 secondes, 423 itérations || heuristique 2 : 14 sec, 962 itérations
# p, C = parse_sat("SAT/jnh1.cnf")
# heuristique 1 : 10sec; 26217 itérations || heuristique 2 : 22 sec, 73186 itérations
# p, C = parse_sat("SAT/aim-50-1_6-no-1.cnf")
# p, C = parse_sat("SAT/uuf125-01.cnf")  # 116895 itérations, 762 secondes
>>>>>>> 8248dda6a8ed69591c7c43901e5d63c8f261f539
# p, C = parse_sat("SAT/logistics.a.cnf")  # 116895 itérations, 762 secondes
CPT_FALSE = 0
CPT_CU = 0

# print(C)
# main_SAT(p, C)

############################################################################################################################################


def generate_lit_id(K_couleurs, sommet_id):
    return [sommet_id*K_couleurs - i for i in range(K_couleurs)][::-1]


def generate_phase1(sommets, K_couleurs):
    C = []
    for sommet in range(1, sommets+1):
        toappend = generate_lit_id(K_couleurs, sommet)
        C.append(toappend)
        temp = list(map(lambda x: x*-1, toappend))
        # print([list(p) for p in itertools.combinations(
        #     map(lambda x: x*-1, toappend), K_couleurs)])
        C.extend(list(map(list, list(itertools.combinations(temp, 2)))))
    return C


def generate_phase2(C, V, K_couleurs):
    for s1, s2 in V:
        coul_s1 = generate_lit_id(K_couleurs, s1)
        coul_s2 = generate_lit_id(K_couleurs, s2)
        C.extend(
            list(map(lambda x: [x[0]*-1, x[1]*-1], zip(coul_s1, coul_s2))))
    return C


def main_graph(file, K_couleurs):
    edges, vertices, V = parse_graph(file)


    C = []
    C = generate_phase1(edges, K_couleurs)
    C = generate_phase2(C, V, K_couleurs)

    p = generate_lit_id(K_couleurs, edges)[-1]
<<<<<<< HEAD
=======
    # print(f" AAAAAAAAAAAAAAAAAAAAAAAAAPour les graphes, p = {p}")
    # print(C)
>>>>>>> 8248dda6a8ed69591c7c43901e5d63c8f261f539

    begin = perf_counter()
    S = backtrack(C, p, test_consistance_heurstique1)  # compteur de littéraux
    end = perf_counter()
    print(f"TEMPS DE CALCUL : {round(end - begin, 2)} secondes")


    cols = ([i for i in sorted(S, key=lambda tup: tup[0]) if i[1] == 1])
    # print(len(cols), cols)
    # print("here", S, len(S), len(S) >= 0)
    if len(list(S)) == 0:
        return False 
    else:
        print(file, file.split(os.sep)[-1])
        with open(join("GRAPH_SOLVED", file.split(os.sep)[-1]), "w") as f:
            for i, e in enumerate(cols):
                f.write(str(i+1) + " " + str((K_couleurs) -
                                            ((i+1)*K_couleurs - e[0])) + "\n")
        return True

<<<<<<< HEAD
# f = "GRAPH\\perso.col"
# f = "GRAPH\\flat20_3_0.col"
# f = "GRAPH/flat20_3_0.col"
# f = "GRAPH\\le450_15a.col"
# f = "GRAPH\\myciel3.col"
# f = "GRAPH\\myciel4.col"
# f = "GRAPH\\queen5_5.col"
# f = "GRAPH\\queen9_9.col"
# main_graph(f, 3)



=======
# f = "color/perso.col"
# f = "color/flat20_3_0.col"
# f = "color/le450_15a.col"
# main_graph(f, 3)


>>>>>>> 8248dda6a8ed69591c7c43901e5d63c8f261f539
def get_affectation(S, var):
    for X, v, _ in S:
        if X == abs(var):
            print(X, v)


def get_affectation_true(S):
    return sum([1 for X, v, _ in S if v == 1])


if __name__ == "__main__":
    pass
