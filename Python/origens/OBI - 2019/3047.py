monica = int(input())
filhos = [int(input()), int(input())]
filhos.append(monica - (filhos[0] + filhos[1]))

print(max(filhos))