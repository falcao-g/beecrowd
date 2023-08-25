alternativas = ['A', 'B', 'C', 'D', 'E']
while True:
    n = int(input())
    if n == 0:
        break
    for _ in range(n):
        notas = [int(a) for a in input().split()]
        resp = ''
        invalido = False
        for n in range(5):
            if notas[n] <= 127 and resp == '':
                resp = alternativas[n]
            elif notas[n] <= 127 and resp != '':
                invalido = True
                break
        if invalido or resp == '':
            print('*')
        else:
            print(resp)