from math import sqrt
line = [float(x) for x in input().split(' ')]

a, b, c = line

delta = b**2-4*a*c

if delta < 0 or a == 0:
    print('Impossivel calcular')
else:
    r1 = (-b+sqrt(delta))/(2*a)
    r2 = (-b-sqrt(delta))/(2*a)
    print(f"R1 = {r1:.5f}")
    print(f"R2 = {r2:.5f}")