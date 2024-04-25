while True:
    try:
        s = input()
        contador = 0

        for c in s:
            if c == '(':
                contador += 1
            elif c == ')':
                contador -= 1

                if contador < 0:
                    break

        print("correct" if contador == 0  else "incorrect")

    except:
        break
