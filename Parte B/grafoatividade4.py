import networkx as nx
import matplotlib.pyplot as plt

arestas = [(1, 2), (1, 3)]

G = nx.Graph()
G.add_edges_from(arestas)

plt.figure(figsize=(6, 6))
pos = nx.spring_layout(G)

nx.draw(G, pos, 
        with_labels=True, 
        node_color='orange', 
        node_size=2000, 
        font_size=16, 
        font_weight='bold', 
        edge_color='black', 
        width=2)

plt.title("Grafo do Exercício 4")
plt.show()