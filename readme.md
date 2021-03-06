## Description de l'archive
Cette archive contient :

- 3 dossiers:
 1. [SAT](src/SAT) : Contient des fichiers .cnf pour représenter les instances de SAT
 2. [GRAPH](src/GRAPH) : Contient des fichiers .col pour représenter les graphes
 3. [GRAPH_SOLVED](src/GRAPH_SOLVED) : Contient la solution (association sommet -> couleur) des instances de graphes dans GRAPH
- 3 fichiers
 1. [DPLL](src/DPLL.py) : Contient mon implémentation de DPLL
 2. [drawgraph](src/drawgraph.py) : Permet de dessiner un graphe avec la librairie *networkx* et *matplotlib*
 3. [main](src/main.py) : le programme qu'il faut lancer pour faire tourner le code


## Utilisation du programme

[Regarder le tutoriel vidéo](https://youtu.be/aEVPTrXO2P0) ou lire les explications si dessous. 

Pour utiliser mon programme, il faut tout simplement lancer le fichier `main.py` et suivre les indications dans la console. Il faudra tout d'abord choisir entre résoudre une instance de **SAT** ou de **Coloration de graphe** puis il faudra choisir un des fichiers contenus dans le [dossier SAT](src/SAT) (si on souhaite résoudre une instance de SAT) ou dans le [dossier GRAPH](src/GRAPH) (si on souhaite résoudre une coloration de graphe). 

Pour SAT il suffit simplement de choisir le fichier désirer (en donnant son numéro dans la liste affiché dans la console). 
Pour GRAPH, il faut, en plus du choix du fichier (comme pour SAT), spécifier le nombre de couleurs (*K*) maximum pour tenter de résoudre l'instance.



## Tableau des résultats (SAT)

|   Fichiers / Critères   | Satisfiable ? | Modèle partiel ?  (nb littéraux) | Nb itérations | Nb erreurs | Nb C.U propagées | Temps de calcul |
|:-----------------------:|:-------------:|:--------------------------------:|:-------------:|:----------:|:----------------:|:---------------:|
|     SAT/uf20-01.cnf     |      OUI      |             19 sur 20            |       48      |      8     |        61        |      0.01s      |
|     SAT/uf50-01.cnf     |      OUI      |             47 sur 50            |       56      |      5     |        112       |      0.05s      |
|     SAT/uuf50-05.cnf    |      NON      |                 /                |      439      |     56     |       1018       |      0.57s      |
|    SAT/uuf125-01.cnf    |      NON      |                 /                |     41273     |    4396    |      128757      |     149.18s     |
|       SAT/jnh1.cnf      |      OUI      |            99 sur 100            |      183      |     11     |        393       |      2.61s      |
| SAT/aim-50-1_6-no-1.cnf |      NON      |                 /                |     24790     |    5503    |       17021      |      8.32s      |
|   SAT/logistics.a.cnf   |   trop long   |                 ?                |       ?       |      ?     |         ?        |        ?        |



|  Fichiers / Critères | Satisfiable ? | Nb couleurs(K) | Temps de calcul | Nb itérations |          Image de le coloration          |
|:--------------------:|:-------------:|:--------------:|:---------------:|:-------------:|:----------------------------------------:|
| GRAPH/flat20_3_0.col |      OUI      |        3       |      0.01s      |       15      | [Voir image](src/img_coloration/flat20_3_0.png) |
|   GRAPH/myciel4.col  |      OUI      |        4       |      0.03s      |       36      |   [Voir image](src/img_coloration/myciel4.png)  |
|   GRAPH/myciel5.col  |      OUI      |        5       |      0.56s      |       83      |   [Voir image](src/img_coloration/myciel5.png)  |
|  GRAPH/queen5_5.col  |      OUI      |        5       |      0.31s      |       32      |  [Voir image](src/img_coloration/queen5_5.png)  |
|  GRAPH/queen9_9.col  |       ?       |        ?       |        ?        |       ?       |                     /                    |
|  GRAPH/le450_15a.col |   trop long   |       15       |        ?        |       ?       |                     /                    |
