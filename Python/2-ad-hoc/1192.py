for _ in range(int(input())):
    n, c, n2 = [x for x in input()]
    n = int(n)
    n2 = int(n2)
    if n == n2:
        print(n * n2)
    elif c.islower():
        print(n + n2)
    else:
        print(n2 - n)