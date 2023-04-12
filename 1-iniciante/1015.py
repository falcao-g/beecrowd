from math import sqrt

line1 = input().split(" ")
line2 = input().split(" ")

x1, y1 = line1
x2, y2 = line2

distance = sqrt((float(x2) - float(x1))**2 + (float(y2) - float(y1))**2)

print(f"{distance:.4f}")