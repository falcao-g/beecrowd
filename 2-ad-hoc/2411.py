import sys

sys.stdin.readline()
x = 4
y = 3
holes = [[1, 3], [2, 3], [2, 5], [5, 4]]
movements = sys.stdin.readline().split()

successful = 0
for movement in movements:
    if movement == '1':
        x += 1
        y += 2
    elif movement == '2':
        x += 2
        y += 1
    elif movement == '3':
        x += 2
        y -= 1
    elif movement == '4':
        x += 1
        y -= 2
    elif movement == '5':
        x -= 1
        y -= 2
    elif movement == '6':
        x -= 2
        y -= 1
    elif movement == '7':
        x -= 2
        y += 1
    elif movement == '8':
        x -= 1
        y += 2

    successful += 1

    if [x, y] in holes:
        break

sys.stdout.write(f'{successful}\n')