inicio, fim = map(int, input().split(" "))

if inicio > fim or inicio == fim:
    fim += 24
    
duracao = fim - inicio

print(f"O JOGO DUROU {duracao} HORA(S)")