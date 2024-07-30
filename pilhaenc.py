class nodo:
    def __init__(self, valor):
        self.info = valor
        self.prox = None

class pilha:
    def __init__(self, valor):
        self.topo = nodo(valor)

    def inserir(self, valor):
        aux = nodo(valor)
        aux.prox = self.topo
        self.topo = aux

    def remover(self):
        if self.topo != None:
            aux = self.topo
            self.topo = aux.prox
            return True
        
        else:
            return False
        
    def buscar(self):
        if self.topo != None:
            return self.topo
        else:
            return None