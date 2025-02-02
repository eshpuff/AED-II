# 3) Implemente de maneira iterativa e recursiva o cálculo de Fibonacci. Consulte a aula para verificar um exemplo.

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacciInterativo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

n = int(input('insira valor: '))
print(fibonacci(n))
print(fibonacciInterativo(n))

