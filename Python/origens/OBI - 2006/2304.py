falcoins, op = map(int, input().split())
d, e, f = falcoins, falcoins, falcoins

def changeFalcoins(user, falcoins):
    global d
    global e
    global f
    if user == 'D':
        d += falcoins
    elif user == 'E':
        e += falcoins
    else:
        f += falcoins

for i in range(op):
    line = input().split()

    if line[0] == 'C':
        changeFalcoins(line[1], -int(line[-1]))
    elif line[0] == 'V':
        changeFalcoins(line[1], int(line[-1]))
    else:
        changeFalcoins(line[1], int(line[-1]))
        changeFalcoins(line[2], -int(line[-1]))

print(d, e, f)