print("\n| Calculador de valor presente do fluxo de caixa |\n")

#Head
caixa = [4000, 1000, 3000, 2500]
i = float(input("Taxa de juros: "))

#Body
print(f"O valor presente do fluxo de caixa é:")

for p in range(len(caixa)):
    caixa[p] = caixa[p] / (1 + i) ** p
    print(f"{caixa[p]:.2f}")
