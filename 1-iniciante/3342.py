tam = int(input()) ** 2

if tam % 2 == 0:
    print(f'{tam // 2} casas brancas e {tam // 2} casas pretas')
else:
    print(f'{tam // 2 + 1} casas brancas e {tam // 2} casas pretas')
