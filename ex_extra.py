class Nodo ():
    def __init__ (self, valor):
        self.info = valor
        self.prox = None

class pilha:
    def __init__ (self):
        self.topo = None

    def inserir(self, valor):
        aux = Nodo(valor)
        aux.prox = self.topo
        self.topo = aux

    def remove(self):
        if self.topo != None:
            self.topo = self.topo.prox
            return True
        else:
            return False

    def consultar(self):
        if self.topo != None:
            return self.topo.info
        else:
            return None

class filaEnc:
    def __init__ (self):
        self.ini = None
        self.fim = None

    def inserir(self, valor):
        elem = Nodo(valor)
        if self.ini == None and self.fim == None:
            self.ini = elem
        else:
            self.fim.prox = elem        
        self.fim = elem
        
    def consultar(self):
        if self.ini != None:
            return self.ini.info
        else:
            return None
    
    def remove(self):
        if self.ini != None:
            if self.ini == self.fim:
                self.fim = None
            self.ini = self.ini.prox

pilhaAux = pilha()
pilha = pilha()

fila = filaEnc()

fila.inserir(10)
fila.inserir(2)
fila.inserir(71)
fila.inserir(16)
fila.inserir(22)


while fila.consultar() != None:

    if pilha.consultar() == None:
        pilha.inserir(fila.consultar())
        fila.remove()

    else:
        if fila.consultar() < pilha.consultar():
            pilha.inserir(fila.consultar())
            fila.remove()
        
        else:
            while fila.consultar() >= pilha.consultar():

                pilhaAux.inserir(pilha.consultar())
                pilha.remove()
            
                if pilha.consultar() == None:
                    break

            pilha.inserir(fila.consultar())
            
            while pilhaAux.consultar() != None:
                pilha.inserir(pilhaAux.consultar())
                pilhaAux.remove()
            fila.remove()

while pilha.consultar() != None:
    fila.inserir(pilha.consultar())
    pilha.remove()
