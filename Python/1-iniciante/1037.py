x = float(input())

if x < 0 or x > 100:
    print('Fora de intervalo')
else:
    if x >= 0 and x <= 25:
        print("Intervalo [0,25]")
    elif x > 25 and x <= 50:
        print("Intervalo (25,50]")
    elif x > 50 and x <= 75:
        print("Intervalo (50,75]")
    else:
        print("Intervalo (75,100]")