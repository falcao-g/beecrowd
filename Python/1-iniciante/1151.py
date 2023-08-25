def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

numeros = [str(fib(i)) for i in range(int(input()))]
print(' '.join(numeros))