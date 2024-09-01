print("\n| Calculador de valor presente de uma série uniforme |\n")

#Head
renda = float(input("Renda da série uniforme: "))
i = float(input("Taxa de desconto da série uniforme: ").replace(",", "."))
p = float(input("Período da série uniforme: "))

#Body
def vp_serie(renda, i, p):
    return renda * ((1 + i) ** p - 1)/((1+i) ** p * i)

print(f"\nO valor presente da série uniforme é R${vp_serie(renda, i, p):.2f}")