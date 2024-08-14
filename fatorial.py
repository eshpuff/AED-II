#2) Implemente de maneira iterativa e recursiva um método que retorne o fatorial de um número natural passado como argumento. Consulte a aula para verificar um exemplo.

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

def fatorialIterativo(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


n = int(input('insira um valor: '))
print(fatorial(n))
print(fatorialIterativo(n))

