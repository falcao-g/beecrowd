v = int(input())
p = int(input())

if (v % p == 0):
    for i in range(p):
        print(v//p)
else:
    a = v % p 
    b = int(v/p)
    
    for i in range(a):
        print(b + 1)

    for i in range(p-a):
        print(v//p)