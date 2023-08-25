def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for i in range(int(input())):
    number = int(input())
    if isPrime(number):
        print(f"{number} eh primo")
    else:
        print(f"{number} nao eh primo")