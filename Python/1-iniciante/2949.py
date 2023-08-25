hobbits = 0
humans = 0
elfs = 0
dwarfs = 0
mages = 0
for i in range(int(input())):
    race = input().split()[1]

    if race == 'X':
        hobbits += 1
    elif race == 'A':
        dwarfs += 1
    elif race == 'E':
        elfs += 1
    elif race == 'H':
        humans += 1
    else:
        mages += 1

print(f"{hobbits} Hobbit(s)")
print(f"{humans} Humano(s)")
print(f"{elfs} Elfo(s)")
print(f"{dwarfs} Anao(oes)")
print(f"{mages} Mago(s)")