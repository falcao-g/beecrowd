letra = input()
texto = input().split()

total = len(texto)
encontrados = 0
for palavra in texto:
    if letra in palavra:
        encontrados += 1
        continue
print(f'{encontrados/total * 100:.1f}')