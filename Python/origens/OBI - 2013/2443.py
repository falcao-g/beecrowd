def euclides(a, b):
    if b == 0:
        return a
    return euclides(b, a % b)

def mmc(a, b):
    return a * b // euclides(a, b)

dividendo1, divisor1, dividendo2, divisor2 = map(int, input().split())

novo_divisor = mmc(divisor1, divisor2)

dividendo1 *= novo_divisor // divisor1
dividendo2 *= novo_divisor // divisor2

novo_dividendo = dividendo1 + dividendo2

divisor = euclides(novo_dividendo, novo_divisor)

print(novo_dividendo // divisor, novo_divisor // divisor)