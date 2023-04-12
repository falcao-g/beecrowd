line1 = input().split(" ")

a, b, c = line1
a = float(a)
b = float(b)
c = float(c)

print(f"TRIANGULO: {(a*c)/2:.3f}")
print(f"CIRCULO: {3.14159 * c**2:.3f}")
print(f"TRAPEZIO: {((a+b)*c)/2:.3f}")
print(f"QUADRADO: {b**2:.3f}")
print(f"RETANGULO: {a*b:.3f}")