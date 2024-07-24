class listCont:
    def __init__(self,max):
        self.max = max
        self.inicio = None
        self.fim = None
        self.vetor = [None] * max
        self.tamanho = 0

    def buscar(self, valor):
        i = self.inicio
        cont = 0

        while i <= self.fim:
            if self.vetor[i] == valor:
                cont += 1
                i += 1
                return cont
        return None

    def valor(self, posicao):
        if posicao >= 0 and posicao <= (self.fim - self.inicio - 1):
            return self.vetor[self.inicio + posicao]
            