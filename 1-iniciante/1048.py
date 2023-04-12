salario = float(input())

if 0 <= salario <= 400:
    reajuste = 15
elif 400 < salario <= 800:
    reajuste = 12
elif 800 < salario <= 1200:
    reajuste = 10
elif 1200 < salario <= 2000:
    reajuste = 7
else:
    reajuste = 4
    
novo_salario = salario + (salario / 100 * reajuste)

print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {novo_salario - salario:.2f}")
print(f"Em percentual: {reajuste} %")