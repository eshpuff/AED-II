# 1) Implemente de maneira iterativa e recursiva a operação soma_elementos(). Esse método deve receber como parâmetro uma lista ou vetor contendo números e retornar a soma dos elementos desta lista. Por exemplo, se v = [1, 2, 3, 10], soma_elementos(v) deve retornar 16.

def somaElementos(v):
    if len(v) == 0:
        return 0
    else:
        return v[0] + somaElementos(v[1:])


def somaIterativa(v):
    soma = 0
    for elemento in v:
        soma += elemento
    return soma

v = [1, 2, 3, 10]

print(somaElementos(v))
print(somaIterativa(v))
