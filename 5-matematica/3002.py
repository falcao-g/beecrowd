from math import sqrt

def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

renda = int(input())

if renda == 2 or renda == 3 or renda == 5 or renda ==7:
    print(1)
elif renda % 2 == 0 or isPrime(renda -2) :
    print(2)
elif not isPrime(renda):
    print(3)
else:
    print(1)