valores = map(int, input().split())
a, b, c = valores

if a > b:
    if b <= c:
        print(":)")
    elif b > c and (b - c) < (a - b):
        print(":)")
    else:
        print(":(")
elif a < b:
    if b >= c:
        print(":(")
    elif b < c and (c - b) < (b - a):
        print(":(")
    else:
        print(":)")
else:
    if b < c:
        print(":)")
    else:
        print(":(")
