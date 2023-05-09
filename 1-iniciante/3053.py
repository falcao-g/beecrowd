n = int(input())
cup = input()
for _ in range(n):
    move = input()
    if move == '1' and not cup == 'C':
        if cup == 'A':
            cup = 'B'
        else:
            cup = 'A'
    elif move == '2' and not cup == 'A':
        if cup == 'B':
            cup = 'C'
        else:
            cup = 'B'
    elif move == '3' and not cup == 'B':
        if cup == 'A':
            cup = 'C'
        else:
            cup = 'A'
print(cup)