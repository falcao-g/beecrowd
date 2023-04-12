numbers = [int(input())]

for i in range(9):
    numbers.append(numbers[-1] * 2)
    
for index, value in enumerate(numbers):
    print(f"N[{index}] = {value}")