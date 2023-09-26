while n := int(input()) != 0:
    games = [int(x) for x in input().split()]

    john = 0
    mary = 0

    for game in games:
        if game == 0:
            mary += 1
            continue
        john += 1

    print(f'Mary won {mary} times and John won {john} times')