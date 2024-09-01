print("\n| Calculadora de Raízes para Polinômios de 2° Grau |\n")

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

x1 = (-b - (b ** 2 - 4 * a * c) ** (1/2)) / (2 * a)
x2 = (-b + (b ** 2 - 4 * a * c) ** (1/2)) / (2 * a)

print(f"\nAs raízes da função {a}x² + {b}x + {c} são:",
      f"\n -> x₁ = {x1:.2f}",
      f"\n -> x₂ = {x2:.2f}")
