import sys

sys.stdin.readline()

values = [int(x) for x in sys.stdin.readline().split()]

if len(values) > 2:
    pattern = True
    for i in range(1, len(values)-1):
        if values[i-1] == values[i] or values[i] == values[i+1] or values[i-1] < values[i] < values[i + 1] or values[i-1] > values[i] > values[i+1]:
            pattern = False
            break
    sys.stdout.write('1\n' if pattern else '0\n')
else:
    sys.stdout.write('1\n' if values[0] != values[1] else '0\n')