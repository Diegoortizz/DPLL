import matplotlib.pyplot as plt
import networkx as nx
from DPLL import parse_graph


customPalette = ['#630C3A', '#39C8C6', '#D3500C', '#FFB139', '#04AF00', '#39A7FF',
                 '#7519CC', '#79E7FF', '#1863C15', '#B72EB9', '#EC2328', '#C86D39']

# customPalette = ['r', 'g', 'b']


def drawGraph(file, filesolve):

    sommets, _, edges = parse_graph(file)

    dico_colors = {i: 0 for i in range(1, sommets + 1)}

    with open(filesolve, 'r') as f:
        L = [(int(p.split()[0]), int(p.split()[-1])) for p in f.readlines()]
        for e, c in L:
            dico_colors[e] = c
    

    G = nx.Graph()
    source_nodes = set([edge[0] for edge in edges])
    G.add_edges_from(edges)

    for n in G.nodes():
        # print(n, dico_colors[n], customPalette[dico_colors[n] - 1])
        G.nodes[n]['color'] = customPalette[dico_colors[n] - 1]

    # pos = nx.spring_layout(G)
    pos = nx.circular_layout(G)

    colors = [node[1]['color'] for node in G.nodes(data=True)]
    nx.draw_networkx(G, pos, with_labels=True, node_color=colors)
    
    plt.show()
