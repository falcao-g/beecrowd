values = []
for i in range(1, 21):
    values.insert(0, int(input()))
    
for index, value in enumerate(values):
    print(f"N[{index}] = {value}")