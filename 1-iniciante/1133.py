x = int(input())
y = int(input())

inc = 1
if x > y:
    inc = -1

numeros = []
for i in range(x, y, inc):
    if i % 5 == 2 or i % 5 == 3:
        numeros.append(i)
        
numeros.sort()
for i in numeros:
    print(i)