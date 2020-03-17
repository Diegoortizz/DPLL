from DPLL import main_SAT, main_graph, parse_sat, parse_graph
from drawgraph import drawGraph
import os
from os.path import isfile, join


instance = ""


dir_path = os.path.dirname(os.path.realpath(__file__))
dir_GRAPH = os.path.join(dir_path, "GRAPH")
dir_GRAPH_SOLVED = os.path.join(dir_path, "GRAPH_SOLVED")
dir_SAT = os.path.join(dir_path, "SAT")

files_GRAPH = [" ".join((f, "(" + str(i + 1) + ")"))
               for i, f in enumerate(os.listdir(dir_GRAPH)) if isfile(join(dir_GRAPH, f))]
files_SAT = [" ".join((f, "(" + str(i + 1) + ")"))
             for i, f in enumerate(os.listdir(dir_SAT)) if isfile(join(dir_SAT, f))]

while True:
    sat_or_graph = input(
        "Test de DPLL avec une instance de SAT (S) ou graphe (G) ? \n S/G ? ")
    if sat_or_graph == "S":
        instance = sat_or_graph
        print("instance de SAT")
        break
    elif sat_or_graph == "G":
        instance = sat_or_graph
        print("instance de Graphe")
        break
    else:
        print("ERREUR, choisir entre 'S' ou 'G'")
        continue
['./SAT/aim-50-1_6-no-1.cnf (1)', './SAT/jnh1.cnf (2)', './SAT/logistics.a.cnf (3)', './SAT/uf20-01.cnf (4)', './SAT/uf50-01.cnf (5)', './SAT/uuf125-01.cnf (6)', './SAT/uuf50-05.cnf (7)']
{1: './SAT/aim-50-1_6-no-1.cnf', 2: './SAT/jnh1.cnf', 3: './SAT/logistics.a.cnf', 4: './SAT/uf20-01.cnf', 5: './SAT/uf50-01.cnf', 6: './SAT/uuf125-01.cnf', 7: './SAT/uuf50-05.cnf'}

if instance == "S":
    filesSAT = files_SAT
    dictSAT = {(i + 1): f for i, f in enumerate(filesSAT)}
    print("HEEEEEEEEEEEEEEEERE", filesSAT)
    # print(dictSAT)
    max_idx = str(len(filesSAT))
    str_to_display = "\n".join(filesSAT)
    while True:
        filechoosen = input(
            f"Choisissez l'instance de SAT à résoudre : \n{str_to_display}\nDonnez le numéro du fichier à résoudre [1 à {max_idx}]: ")
        try:
            file_to_solve = os.path.join("SAT", (dictSAT[int(filechoosen)]))
            # file_to_solve = "SAT/" + (dictSAT[int(filechoosen)])
            break
        except KeyError:
            print("Numéro de fichier invalide")
            continue

    print("----"*25)
    print(f"DEBUT DE LA RESOLUTION DE {file_to_solve.split()[0]}")
    p, C = parse_sat(file_to_solve.split()[0])
    print("... résolution en cours ...")
    main_SAT(p, C)


if instance == "G":
    filesGRAPH = files_GRAPH
    dictGRAPH = {(i + 1): f.split()[0] for i, f in enumerate(filesGRAPH)}
    max_idx = str(len(filesGRAPH))
    str_to_display = "\n".join(filesGRAPH)
    while True:
        filechoosen = input(
            f"Choisissez l'instance de SAT à résoudre : \n{str_to_display}\nDonnez le numéro du fichier à résoudre [1 à {max_idx}]: ")
        try:
            file_to_solve = os.path.join(
                "GRAPH", (dictGRAPH[int(filechoosen)]))
            # file_to_solve = "GRAPH/" + (dictGRAPH[int(filechoosen)])
            break
        except:
            print("Numéro de fichier invalide")
            continue

    while True:
        k_choosenstr = input(f"Choisissez le nombre de couleurs K (K >= 1) : ")
        try:
            K = int(k_choosenstr)
            break
        except:
            continue

    print("----"*25)
    print(f"DEBUT DE LA RESOLUTION DE {file_to_solve}")
    print("... résolution en cours ...")
    R = main_graph(file_to_solve, K)
    if R:
        print("Vous pouvez voir la couleur assigné à chaque sommet dans",
              "SOLVED/" + file_to_solve.split("/")[-1])
        if K <= 12:
            rep = input(
                "Voulez vous afficher une représentation du graphe colorié ? (Y/N)")
            if rep == "Y":
                drawGraph(file_to_solve, os.path.join("GRAPH_SOLVED", file_to_solve.split(os.sep)[-1]))
    else:
        print(
            f"On ne peut pas colorier {file_to_solve.split('/')[-1]} avec K = {K}")
