dict = {
    'tesoura':  ['papel', 'lagarto'],
    'papel':  ['pedra', 'Spock'],
    'pedra':  ['tesoura', 'lagarto'],
    'Spock': ['pedra', 'tesoura'],
    'lagarto': ['Spock', 'papel']
}

for i in range(int(input())):
    v1, v2 = map(str, input().split())

    if v2 in dict.get(v1):
        print(f'Caso #{i+1}: Bazinga!')
    elif v1 in dict.get(v2):
        print(f'Caso #{i+1}: Raj trapaceou!')
    else:
        print(f'Caso #{i+1}: De novo!')