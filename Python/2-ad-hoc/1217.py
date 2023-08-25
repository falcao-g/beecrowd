n = int(input())
peso_total = 0
gasto_total = 0
for i in range(n):
    gasto_total += float(input())
    frutas = len(input().split())
    peso_total += frutas
    print(f"day {i+1}: {frutas} kg")
print(f"{peso_total/n:.2f} kg by day")
print(f"R$ {gasto_total/n:.2f} by day")