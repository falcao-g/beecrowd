papagaio = {
    "esquerda": "ingles",
    "direita": "frances",
    "nenhuma": "portugues",
    "as duas": "caiu"
}

while True:
    try:
        lado = input()
        print(papagaio[lado])
    except EOFError:
        break

