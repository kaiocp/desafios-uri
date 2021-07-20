N1, N2, N3, N4 = map(float, input().split())
N5 = 0

media = ((N1*2) + (N2*3) + (N3*4) + N4) / 10

print(f"Media: {media:.1f}")

if (media >= 7):
    print("Aluno aprovado.")
elif (media < 5):
    print("Aluno reprovado.")
elif ((media >= 5) and (media < 7)):
    print("Aluno em exame.")
    N5 = float(input())
    print(f"Nota do exame: {N5}")
    media = (media + N5) / 2
    if (media >= 5):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {media:.1f}")
