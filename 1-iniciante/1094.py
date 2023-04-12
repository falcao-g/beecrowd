coelhos = 0
ratos = 0
sapos = 0
for i in range(int(input())):
    arg = input().split(" ")
    if arg[1] == 'C':
        coelhos += int(arg[0])
    elif arg[1] == 'R':
        ratos += int(arg[0])
    else:
        sapos += int(arg[0])
        
total = coelhos + sapos + ratos
        
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {coelhos / total * 100:.2f} %")
print(f"Percentual de ratos: {ratos / total * 100:.2f} %")
print(f"Percentual de sapos: {sapos / total * 100:.2f} %")