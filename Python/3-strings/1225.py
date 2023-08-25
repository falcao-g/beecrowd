template = {c : 0 for c in 'abcdefghijklmnopqrstuvwxyz'}

for _ in range(int(input())):
    letras = template.copy()
    texto = input().lower()

    for c in texto:
        if c.isalpha():
            letras[c] += 1

    maior_ocorrencia = max(letras.values())

    for k, v in letras.items():
        if v == maior_ocorrencia:
            print(k, end='')
    print()