par = []
impar = []
for i in range(15):
    numero = int(input())
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

    if len(par) == 5:
        for j in range(len(par)):
            print(f'par[{j}] = {par[j]}')
        par = []
    if len(impar) == 5:
        for j in range(len(impar)):
            print(f'impar[{j}] = {impar[j]}')
        impar = []

for j in range(len(impar)):
    print(f'impar[{j}] = {impar[j]}')

for j in range(len(par)):
    print(f'par[{j}] = {par[j]}')