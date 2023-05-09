alfabeto = 'abcdefghijklmnopqrstuvwxyz'
novo_alfabeto = {}
permuta = input()
for c in range(len(permuta)):
    novo_alfabeto[alfabeto[c]] = permuta[c]

mensagem = input()
descriptada = ''
for l in mensagem:
    descriptada += novo_alfabeto.get(l)

print(descriptada)