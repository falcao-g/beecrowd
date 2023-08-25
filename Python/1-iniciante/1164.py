for i in range(int(input())):
    number = int(input())
    
    soma = 0
    for i in range(1, number):
        if number % i == 0:
            soma += i
            
        if soma > number:
            break
        
    if soma == number:
        print(f"{number} eh perfeito")
    else:
        print(f"{number} nao eh perfeito")