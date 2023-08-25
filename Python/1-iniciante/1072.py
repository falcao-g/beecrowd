dentro = 0
fora = 0
for i in range(int(input())):
    x = int(input())
    
    if 10 <= x <= 20:
        dentro += 1
    else:
        fora += 1
        
print(f"{dentro} in")
print(f"{fora} out")