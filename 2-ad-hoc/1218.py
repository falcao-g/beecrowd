texto = []
caso = 0
while True:
    try:
        numero = input()
        caso += 1
        tenis = [a for a in input().split()]
        iguais = 0
        masc = 0
        fem = 0
        for i in range(0, len(tenis), 2):
            if tenis[i] == numero:
                iguais += 1
                if tenis[i+1] == 'M':
                    masc += 1
                else:
                    fem += 1
        texto.append(f'Caso {caso}:\nPares Iguais: {iguais}\nF: {fem}\nM: {masc}')
    except EOFError:
        break
print('\n\n'.join(texto))