posicoes = [int(p) for p in input().split()]

posicao_kung = posicoes.index(1)
posicao_lu = posicoes.index(9)

if posicao_kung // 2 == posicao_lu // 2:
    fase = "oitavas"
elif posicao_kung // 4 == posicao_lu // 4:
    fase = "quartas"
elif posicao_kung // 8 == posicao_lu // 8:
    fase = "semifinal"
else:
    fase = "final"

print(fase)