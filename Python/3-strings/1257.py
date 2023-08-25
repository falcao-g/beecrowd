for _ in range(int(input())):
    hash = 0
    for el in range(int(input())):
        for index, value in enumerate(input()):
            hash += ord(value) - 65 + el + index
    print(hash)