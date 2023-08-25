print("MUITO OBRIGADO")

alcool = 0
gasolina = 0
diesel = 0
while True:
    numero = int(input())

    if numero == 1:
        alcool += 1
    elif numero == 2:
        gasolina += 1
    elif numero == 3:
        diesel += 1
    elif numero == 4:
        break
    
print(f"Alcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")