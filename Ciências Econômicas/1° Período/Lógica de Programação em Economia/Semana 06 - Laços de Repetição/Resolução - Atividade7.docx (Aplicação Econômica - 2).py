print("\n| Calculador de valor presente líquido |\n")

#Head
custo = 4000
renda = [1000, 3000, 2500]
pvl = 0


#Body
for p in range(len(renda)):
    pvl += renda[p] / (1 + renda[p] / custo) ** p

print(f"O valor presente líquido do investimento inicial de {custo:.2f} é de {pvl:.2f}")

if custo >= pvl:
    print("Dessa forma, o investimento é inviável")
else:
    print("Dessa forma, o investimento é viável")