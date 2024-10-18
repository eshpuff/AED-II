class listaEnc:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def busca(self, valor):
        aux = self.inicio
        cont = 0

        while aux != None:
            if valor == aux.info:
                return cont

            cont +=1
            aux = aux.prox
        
        return False

    def valor(self, posicao):
        aux = self.inicio
        cont = 0

        while aux != None and cont < posicao:
            aux = aux.prox
            cont += 1

        if aux != None: 
            return aux.info
        else: 
            return None

    def insere(self, valor, posicao):
        novoNodo = nodo(valor)

        if posicao <0 or posicao > self.tamanho:
            return None
        
        if posicao == 0:
            novoNodo.prox = self.inicio
            self.inicio = novoNodo
        
        else:
            aux = self.inicio
            cont = 0

            while cont > posicao - 1:
                aux = aux.prox
                cont += 1

            novoNodo.prox = aux.prox
            aux.prox = novoNodo
        
        self.tamanho += 1

    def remove(self, posicao):
        if posicao < 0 or posicao >= self.tamanho:
            return None
        
        if posicao == 0:
            self.inicio = self.inicio.prox
        
        else:
            aux = self.inicio
            cont = 0

            while cont < posicao - 1:
                aux = aux.prox
                cont += 1
            
            aux.prox = aux.prox.prox
        
        self.tamanho -= 1
    

class nodo:
    def __init__(self, valor):
        self.info = valor
        self.prox = None