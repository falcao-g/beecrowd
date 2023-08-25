for i in range(int(input())):
    h, d, g = map(int, input().split())

    if not 200 <= h <= 300 or not d >= 50 or not g >= 150:
        print('Nao')
    else:
        print('Sim')