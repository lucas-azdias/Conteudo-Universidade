print("\n| Média das notas de quatro alunos fornecidas pelo usuário |\n")

#Head
notas = list()
média = 0

#Body
for i in range(4):
    notas.append(float(input(f"Nota do Aluno {i + 1}: ")))
    média += notas[i]

média = média / 4

print(f"\nA média dos alunos foi: {média:.2f}, sendo que:")

for i in range(4):
    if notas[i] >= 7:
        print(f"    > Aluno {i + 1}: Aprovado")
    elif 4 <= notas[i] < 7:
        print(f"    > Aluno {i + 1}: Em recuperação")
    else:
        print(f"    > Aluno {i + 1}: Reprovado")