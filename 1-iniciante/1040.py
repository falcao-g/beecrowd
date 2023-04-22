nota1, nota2, nota3, nota4 = map(float, input().split())

media = (nota1 * 2 + nota2 * 3 + nota3 * 4 + nota4) / 10

print(f"Media: {media:.1f}")

if media >= 7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    
    nota5 = float(input())
    media2 = (media + nota5) / 2
    print(f"Nota do exame: {nota5:.1f}")
    
    if media2 >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {media2:.1f}")