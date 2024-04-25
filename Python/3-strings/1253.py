n = int(input())

for i in range(n):
    s = input()
    d = int(input())
    ans = ''

    for c in s:
        c = chr(ord(c) - d)

        if ord(c) < 65:
            c = chr(ord(c) + 26)

        ans += c

    print(ans)
