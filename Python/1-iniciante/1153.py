def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)
    
print(fatorial(int(input())))