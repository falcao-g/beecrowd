while True:
    num1, num2 = map(int, input().split(" "))
    x = min(num1, num2)
    y = max(num1, num2)
    
    if x <= 0 or y <= 0:
        break
    else:
        string = ''
        soma = 0
        for i in range(x, y+1):
            string += str(i) + ' '
            soma += i
        print(f"{string}Sum={soma}")