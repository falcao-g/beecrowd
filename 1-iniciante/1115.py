while True:
    num1, num2 = map(int, input().split(" "))
    
    if num1 > 0 and num2 > 0:
        print("primeiro")
    elif num1 < 0 and num2 > 0:
        print("segundo")
    elif num1 < 0 and num2 < 0:
        print("terceiro")
    elif num1 > 0 and num2 < 0:
        print("quarto")
    else:
        break