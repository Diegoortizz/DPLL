README DPLL

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

