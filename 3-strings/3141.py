nome = input()
d1, m1, a1 = map(int, input().split('/'))
d2, m2, a2 = map(int, input().split('/'))

if (d1 >= d2 and m1 == m2) or m1 > m2:
    anos = a1 - a2
else:
    anos = a1 - a2 - 1

if d1 == d2 and m1 == m2:
    print(f"Feliz aniversario!\nVoce tem {anos} anos {nome}.")
else:
    print(f"Voce tem {anos} anos {nome}.")