Mi, Mj = map(int, input().split())
Ii, Ij = map(int, input().split())
Fi, Fj = map(int, input().split())

N_armarios = (Mi//2) * (Mj//2)

if (Mi % 4 == 3) or (Mj % 4 == 3):
    espacos_vazios = 0 if ((abs(Ii - Fi)) + (abs(Ij - Fj))) %4 == 2 else 2
else:
    espacos_vazios = 2 if ((abs(Ii - Fi)) + (abs(Ij - Fj))) %4 == 2 else 0
print((Mi * Mj) - (N_armarios * 2) - (espacos_vazios))