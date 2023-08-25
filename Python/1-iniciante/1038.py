line = [int(x) for x in input().split(' ')]
x, y = line

codes = [4, 4.50, 5, 2, 1.50]
total = codes[x-1] * y

print(f"Total: R$ {total:.2f}")