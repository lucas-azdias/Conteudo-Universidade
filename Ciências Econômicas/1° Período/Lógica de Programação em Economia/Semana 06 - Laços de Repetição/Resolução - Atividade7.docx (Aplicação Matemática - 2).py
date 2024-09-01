print("\n| Cálculo da média da sala |\n")

#Head
notas = [68, 80, 50, 57, 90, 95, 78, 30, 90, 100]


#Body
média = 0

for i in range(len(notas)):
    média += notas[i]

"""

Ou fazendo: média = sum(notas)

"""

média = média / len(notas)

print(f"A média da sala é de: {média}\n")