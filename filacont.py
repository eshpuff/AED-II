class nodo:
    def __init__(self, valor):
        self.info = valor
        self.prox = None

class filaCont:
    def __init__(self, max):
        self.max = max
        self.ini = None
        self.fim = None
        self.vetor = max * [None]
        self.tamanho = 0
        
    def insere(self, valor):
        if self.ini == None:
            self.ini = 0
            self.fim = 0
            self.vetor[self.ini] = valor
            
        elif self.max > self.tamanho():     
            if self.fim == self.max-1:
                self.fim = 0
            else:
                self.fim += 1
            
            self.vetor[self.fim] = valor
            self.tamanho += 1 

    def buscar(self):
        if self.tamanho == 0:
            return None
        return self.vetor[self.ini]
        
    def remove(self):
        if self.tamanho() > 0:
            self.vetor[self.ini] = None
            self.ini = self.ini + 1

            
 
            
                                             

var = filaCont(5)
var.insere(10)

print(var.vetor)

var.insere(20)