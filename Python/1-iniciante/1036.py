import math
import sys
line = map(float, sys.stdin.readline().split())

a, b, c = line

delta = b**2-4*a*c

if delta < 0 or a == 0:
    sys.stdout.write('Impossivel calcular\n')
else:
    r1 = (-b+math.sqrt(delta))/(2*a)
    r2 = (-b-math.sqrt(delta))/(2*a)
    sys.stdout.write(f"R1 = {r1:.5f}\n")
    sys.stdout.write(f"R2 = {r2:.5f}\n")