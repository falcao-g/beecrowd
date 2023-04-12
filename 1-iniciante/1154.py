idade = int(input())
media = 0
cont = 0
while idade >= 0:
    media += idade
    cont += 1
    idade = int(input())
    
print(f"{media/cont:.2f}")