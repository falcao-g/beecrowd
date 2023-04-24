import sys
present = []

for i in range(int(sys.stdin.readline())):
    student = sys.stdin.readline()
    present.append(student)

sys.stdout.write(f'{len(set(present))}\n')