name = str(input())
salary = float(input())
sold = float(input())

total = salary + (sold / 100 * 15)

print(f"TOTAL = R$ {total:.2f}", end="\n")