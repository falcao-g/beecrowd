numeros = [int(x) for x in input().split(" ")]
num1 = numeros[0]
num2 = numeros[-1]

soma = 0
for i in range(num1, num1 + num2):
    soma += i

print(soma)