numeros = []
for i in range(6):
    numeros.append(float(input()))
    
total = 0
media = 0
for numero in numeros:
    if numero > 0:
        total += 1
        media += numero

media /= total
        
print(f"{total} valores positivos")
print(f'{media:.1f}')