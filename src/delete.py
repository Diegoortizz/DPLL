import os 
from os.path import isfile, join
dir_path = os.path.dirname(os.path.realpath(__file__))

dir_GRAPH = os.path.join(dir_path, "GRAPH")
dir_GRAPH_SOLVED = os.path.join(dir_path, "GRAPH_SOLVED")
dir_SAT = os.path.join(dir_path, "SAT")

onlyfiles = [f for f in os.listdir(dir_GRAPH) if isfile(join(dir_GRAPH, f))]
print(onlyfiles)

onlyfiles = [f for f in os.listdir(dir_GRAPH_SOLVED) if isfile(join(dir_GRAPH_SOLVED, f))]
print(onlyfiles)

onlyfiles = [f for f in os.listdir(dir_SAT) if isfile(join(dir_SAT, f))]
print(onlyfiles)

