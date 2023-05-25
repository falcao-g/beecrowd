teste = 1
while True: 
    n = int(input()) 

    if n == 0:
        break

    calc = input()
    operadores = []

    for i in range(len(calc)):
        if not calc[i].isnumeric():
            operadores.append(calc[i])

    calc = calc.replace("-", "+").split("+")
    for i in range(len(calc)):
        calc[i] = int(calc[i])

    conta = calc[0]

    for j in range(len(operadores)):
        if operadores[j] == "+": 
            conta += calc[j + 1]
        else:
            conta -= calc[j + 1]

    print(f"Teste {teste}")
    print(conta)
    print()
    teste += 1