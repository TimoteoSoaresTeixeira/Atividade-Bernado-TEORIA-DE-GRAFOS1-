class Grafo:
    def __init__(self):
        self.lista_adj = {}

    def adicionar_aresta(self, u, v):
        if u not in self.lista_adj:
            self.lista_adj[u] = []
        if v not in self.lista_adj:
            self.lista_adj[v] = []
        
        self.lista_adj[u].append(v)
        self.lista_adj[v].append(u)

    def obter_grau(self, u):
        if u in self.lista_adj:
            return len(self.lista_adj[u])
        return 0

    def total_arestas(self):
        soma = 0
        for u in self.lista_adj:
            soma += len(self.lista_adj[u])
        return soma // 2


g = Grafo()
g.adicionar_aresta(1, 2)
g.adicionar_aresta(2, 3)
g.adicionar_aresta(3, 4)
g.adicionar_aresta(4, 1)

print(g.lista_adj)
print(g.obter_grau(2))
print(g.total_arestas())