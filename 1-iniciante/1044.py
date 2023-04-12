x, y = map(int, input().split(" "))

if x % y == 0 or y % x == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")