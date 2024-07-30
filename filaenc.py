class nodo:
    def __init__(self, valor):
        self.info = valor
        self.prox = None
        
class filaEnc:
    def __init__ (self):
        self.ini = None
        self.fim = None

    def inserir(self, valor):
        elem = nodo(valor)
        if self.ini == None and self.fim == None:
            self.ini = elem
        else:
            self.fim.prox = elem        
        self.fim = elem
        
    def buscar(self):
        if self.ini != None:
            return self.ini.info
        else:
            return None
    
    def remove(self):
        if self.ini != None:
            if self.ini == self.fim:
                self.fim = None
            self.ini = self.ini.prox

            
            
var = filaEnc()
var.inserir(10)
var.inserir(20)
var.inserir(30)
print(var.buscar())
var.remove()
print(var.buscar())