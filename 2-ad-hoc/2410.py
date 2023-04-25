import sys
present = set()

for i in range(int(sys.stdin.readline())):
    present.add(sys.stdin.readline())

sys.stdout.write(f'{len(present)}\n')