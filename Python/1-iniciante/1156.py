s = 1
aux = 2
for i in range(3, 40, 2):
    s += i/aux
    aux *= 2
    
print(f"{s:.2f}")