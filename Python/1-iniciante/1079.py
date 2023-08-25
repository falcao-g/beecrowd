for i in range(int(input())):
    nota1, nota2, nota3 = map(float, input().split(" "))
    media = (nota1 * 2 + nota2 * 3 + nota3 * 5) / (10)
    print(f"{media:.1f}")