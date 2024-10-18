class listCont:
    def __init__(self,max):
        self.max = max
        self.ini = None
        self.fim = None
        self.vetor = [None] * max
        self.tamanho = 0

    def buscar(self, valor):
        i = self.ini
        cont = 0

        while i <= self.fim:
            if self.vetor[i] == valor:
                cont += 1
                i += 1
                return cont
        return None

    def valor(self, posicao):
        if posicao >= 0 and posicao <= (self.fim - self.ini - 1):
            return self.vetor[self.ini + posicao]
    
    def vazia(self):
        return self.ini == -1 or self.fim == -1
            
    def tamanho(self):
        if self.vazia():
            return 0
        else:
            return self.fim - self.ini + 1

    def inserir(self, posicao, dado):
        if ((self.ini != 0 or self.fim != self.max - 1) and posicao > 0 and posicao <= self.tamanho() + 1): # Verificar se existe espaço e se a posicão é válida
            if self.vazia():
                self.ini = 0
                self.fim = 0
            elif self.fim != self.max -1: #deslocar para o fim
                for i in range(self.fim, self.ini + posicao - 2, -1):
                      self.vetor[i + 1] = self.vetor[i]
                self.fim += 1
            else: # deslocar para o inicio
                for i in range(self.fim, self.ini + posicao):
                    self.vetor[i-1] = self.vetor[i]
                self.ini -= 1
            self.vetor[self.ini + posicao - 1] = dado
            return True
        else:
            return False
            