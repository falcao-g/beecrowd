def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

for i in range(int(input())):
    term = int(input())
    print(f"Fib({term}) = {fib(term)}")