for i in range(int(input())):
    texto = [x if x.islower() else '' for x in input()[::-1]]
    print(''.join(texto))