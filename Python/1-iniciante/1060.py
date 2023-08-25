numeros = []
for i in range(6):
    numeros.append(float(input()))
    
total = 0
for numero in numeros:
    if numero > 0:
        total += 1
        
print(f"{total} valores positivos")