# 4) Implemente de maneira recursiva o método soma_digitos(). Este método recebe como parâmetro um número natural e retorna a soma dos dígitos. Por exemplo, somaDigitios(14) deve retornar 5.
 
def somaDigitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + somaDigitos(n // 10)

n = int(input('insira valor: '))
print(somaDigitos(n))
