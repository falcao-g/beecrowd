line = [float(x) for x in input().split(" ")]
line.sort(reverse=True)
a, b, c = line

if a >= b + c:
    print("NAO FORMA TRIANGULO")
else:
    if a**2 == b**2 + c**2:
        print("TRIANGULO RETANGULO")
    elif a**2 > b**2 + c**2:
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")
        
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    
    if a == b != c or b == c != a or a == c != b:
        print("TRIANGULO ISOSCELES")