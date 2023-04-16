import math
import sys

def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

renda = int(input())

if renda == 2 or renda == 3 or renda == 5 or renda ==7:
    sys.stdout.write('1\n')
elif renda % 2 == 0 or isPrime(renda -2) :
    sys.stdout.write('2\n')
elif not isPrime(renda):
    sys.stdout.write('3\n')
else:
    sys.stdout.write('1\n')