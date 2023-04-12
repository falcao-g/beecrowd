money = float(input())
notes = [100, 50, 20, 10, 5, 2]

print("NOTAS:")
for note in notes:
    print(f"{int(money/note)} nota(s) de R$ {note}.00")
    money -= int(money/note) * note
    

money = round(money * 100)
coins = [100, 50, 25, 10, 5, 1]
print("MOEDAS:")
for coin in coins:
    if coin != 1:
        print(f"{int(money/coin)} moeda(s) de R$ {coin/100:.2f}")
        money %= coin
    else:
        print(f"{int(money%5)} moeda(s) de R$ {coin/100:.2f}")