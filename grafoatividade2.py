import networkx as nx
import matplotlib.pyplot as plt

arestas = [(1, 2), (1, 3), (1, 4), (1, 5)]

G = nx.Graph()
G.add_edges_from(arestas)

plt.figure(figsize=(6, 6))
pos = nx.spring_layout(G)

nx.draw(G, pos, 
        with_labels=True, 
        node_color='lightblue', 
        node_size=2000, 
        font_size=16, 
        font_weight='bold', 
        edge_color='gray', 
        width=2)

plt.title("Grafo Estrela (Star Graph)")
plt.show()