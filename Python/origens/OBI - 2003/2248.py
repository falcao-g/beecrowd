turma = 1
while True:
    n = int(input())
    if (n == 0):
        break
    
    entradas = {}
    for i in range(n):
        estudante, media = map(int, input().split())
        entradas[estudante] = media
    
    estudantes = []
    for chave, valor in entradas.items():
        if (valor == max(entradas.values())):
            estudantes.append(chave)
    mensagem = " ".join(map(str, estudantes))
    
    print(f"Turma {turma}")
    print(f"{mensagem} ")
    print()
    turma += 1