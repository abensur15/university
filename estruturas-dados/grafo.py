class Grafo:
    def __init__(self, vertices, direcionado):
        self.vertices = vertices
        self.adjacencias = [[] for _ in range(vertices)]
        self.direcionado = direcionado
    
    def consultar_peso(self, u, v):
        for vertice, peso in self.adjacencias[u]:
            if vertice == v:
                return peso
        
        return None
    
    def inserir_aresta(self, u, v, peso):
        self.adjacencias[u].append((v, peso))
        
        if not self.direcionado:
            self.adjacencias[v].append((u, peso))
    
    def remover_aresta(self, u, v):
        self.adjacencias[u] = [(vertice, peso) for vertice, peso in self.adjacencias[u] if vertice != v]
        
        if not self.direcionado:
            self.adjacencias[v] = [(vertice, peso) for vertice, peso in self.adjacencias[v] if vertice != u]