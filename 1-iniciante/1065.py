numeros = []
for i in range(5):
    numeros.append(int(input()))
    
total = 0
for numero in numeros:
    if numero % 2 == 0:
        total += 1

        
print(f"{total} valores pares")