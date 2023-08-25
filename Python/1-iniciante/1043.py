x, y, z = map(float, input().split(" "))

if x + y > z and y + z > x and x + z > y:
    print(f"Perimetro = {x+y+z:.1f}")
else:
    print(f"Area = {(x+y)*z/2:.1f}")