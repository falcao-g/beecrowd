import sys
for i in range(int(sys.stdin.readline())):
    dieta = set([x for x in sys.stdin.readline().rstrip()])
    manha = set([x for x in sys.stdin.readline().rstrip()])
    almoco = set([x for x in sys.stdin.readline().rstrip()])

    if manha.difference(dieta) or almoco.difference(dieta):
        sys.stdout.write('CHEATER\n')
    else:
        sys.stdout.write(f"{''.join(sorted(dieta.difference(manha.union(almoco))))}\n")