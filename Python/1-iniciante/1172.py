x = []
for i in range(10):
    number = int(input())
    x.append(1 if number <= 0 else number)
    
for index, value in enumerate(x):
    print(f"X[{index}] = {value}")