money = int(input())
notes = [100, 50, 20, 10, 5, 2, 1]

print(money)
for note in notes:
    print(f"{int(money/note)} nota(s) de R$ {note},00")
    money -= int(money/note) * note