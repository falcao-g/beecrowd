array = []
for i in range(100):
    value = float(input())
    array.append(value)
    
    if value <= 10:
        print(f"A[{i}] = {value}")