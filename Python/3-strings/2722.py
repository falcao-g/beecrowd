for _ in range(int(input())):
    line1 = input()
    line2 = input()
    for i in range(len(line1)):
        if i % 2 != 0:
            continue
        print(line1[i:i+2], end='')
        print(line2[i:i+2], end='')
    print('\n', end='')