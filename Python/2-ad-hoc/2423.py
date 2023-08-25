values = [int(x) for x in input().split()]
print(f'{min([values[0] // 2, values[1] // 3, values[2] // 5])}')