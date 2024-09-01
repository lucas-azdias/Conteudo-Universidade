"""

Simplificando as fórmulas:
    
    | Qo = Qd = Q (No equilíbrio)
    | Qo = a + b * P
    | Qd = c - d * P
        -> input: a, b, c, d
        -> output: Q, P

    Qo = Qd
    a + b * P = c - d * P
    (b + d) * P = c - a
  >>P = (c - a) / (b + d)

  >>Q = a + b * P
        or
  >>Q = c - d * P

"""

print("\n| Calculadora de quantidades e de preços no equilíbrio da Oferta e da Demanda |\n")

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = float(input("d: "))

P = (c - a) / (b + d)
Q = a + b * P

print(f"\nPara esse equilíbrio da Oferta e da Demanda, tem-se:",
      f"\n -> Quantidade(Q): {Q:.2f}",
      f"\n -> Preço(P): {P:.2f}")
