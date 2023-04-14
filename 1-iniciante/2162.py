int(input())

values = [int(x) for x in input().split()]

if len(values) > 2:
    pattern = True

    for i in range(1, len(values)-1):
        if values[i-1] < values[i] > values[i + 1] or values[i-1] > values[i] < values[i+1]:
            continue
        else:
            pattern = False
            break

    if pattern:
        print(1)
    else:
        print(0)
else:
    if values[0] != values[1]:
        print(1)
    else:
        print(0)