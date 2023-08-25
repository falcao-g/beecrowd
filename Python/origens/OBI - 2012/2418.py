import sys
values = [float(x) for x in sys.stdin.readline().split()]
values.sort()
sys.stdout.write(f'{values[1] + values[2] + values[3]:.1f}\n')