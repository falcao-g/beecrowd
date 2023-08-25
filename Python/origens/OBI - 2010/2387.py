n = int(input())
consultas = [{'inicio': 0, 'fim': 0} for i in range(n)]

for i in range(n):
    inicio, fim = map(int, input().split())
    consultas[i]['inicio'] = inicio
    consultas[i]['fim'] = fim

consultas.sort(key=lambda x: x['fim'])

qtd = 1
fim = consultas[0]['fim']

for i in range(1, n):
    if consultas[i]['inicio'] >= fim:
        qtd += 1
        fim = consultas[i]['fim']

print(qtd)
