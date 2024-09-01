print("\n| Calculador do multiplicador keynisiano e da renda de equilíbrio de uma economia fechada |\n")

'''

Simplificando as fórmulas, temos: 

    | Y = C + I + G
    | C = C0 + c * Y
    | I = I0
    | G = G0
    | 0 < c < 1
        -> input: C0, I0, G0, c
        -> output: Y, k

    Y = C0 + c * Y + I0 + G0
    (1 - c) * Y = C0 + I0 + G0
    Y = (C0 + I0 + G0) / (1 - c)

    k = 1 / (1 - c)
    Y = (C0 + I0 + G0) * k

'''

#Head
consumo = float(input("Consumo autônomo (de subsistência): ")) #C0
invest = float(input("Investimentos privados na economia: ")) #I0
gastosGov = float(input("Gastos governamentais: ")) #G0
margProp = 0 #c
while not (0 < margProp < 1):
    margProp = float(input("Propenção marginal de consumo para satisfação (entre 0 e 1): "))

numK = 0 #k
pib = 0 #Y

#Body
numK = 1 / (1 - margProp)
pib = (consumo + invest + gastosGov) * numK

print(f"\nMultiplicador keynisiano: {numK:.2f}",
      f"\nPIB de equilíbrio (nessa economia fechada): {pib:.2f}")
