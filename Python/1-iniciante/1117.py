cont = 0
media = 0
while cont < 2:
    nota = float(input())
    
    if 0 <= nota <= 10:
        media += nota
        cont += 1
    else:
        print("nota invalida")

media /= 2        
print(f"media = {media:.2f}")