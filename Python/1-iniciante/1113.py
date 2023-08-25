while True:
    num1, num2 = map(int, input().split(" "))
    
    if num1 > num2:
        print("Decrescente")
    elif num1 < num2:
        print("Crescente")
    else:
        break