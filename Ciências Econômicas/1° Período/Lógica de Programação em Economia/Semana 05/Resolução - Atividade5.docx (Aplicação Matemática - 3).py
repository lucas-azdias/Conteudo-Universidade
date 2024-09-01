print("\n| Calculador de distância entre dois pontos |\n")

from math import sqrt

#Head
A = (float(input("Valor de X para o ponto A: ")), float(input("Valor de Y para o ponto A: ")))
B = (float(input("Valor de X para o ponto B: ")), float(input("Valor de Y para o ponto B: ")))

dist = 0

#Body
dist = sqrt((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2)

print(f"A distância entre os pontos A e B é: {dist:.2f}")