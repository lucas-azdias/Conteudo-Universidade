print("\n| Cálculo de raízes de funções quadráticas |\n")

#Head
a = float(input("Valor da constante a: "))
b = float(input("Valor da constante b: "))
c = float(input("Valor da constante c: "))

delta = (b ** 2) - (4 * a * c)
x1 = 0
x2 = 0

def strComplex(x = complex(0, 0), **kwargs):
    nDigits = kwargs.get("nDigits")
    if nDigits:
        real = round(x.real, nDigits)
        imag = round(x.imag, nDigits)
    else:
        real = x.real
        imag = x.imag
    
    strX = f"{real}"
    
    if imag >= 0:
        strX += f" + {imag}"
    else:
        strX += f" - {abs(imag)}"

    return strX

#Body
x1 = (-b + delta ** (1 / 2)) / (2 * a)
x2 = (-b - delta ** (1 / 2)) / (2 * a)

print(x1, x2)
print(delta)

if delta == 0:
    print(f"As duas raízes são reais e iguais, onde: x₁ = x₂ = {x1:.2f}")

elif delta > 0:
    print(f"As duas raízes são reais e diferentes, onde: x₁ = {x1:.2f} e x₂ = {x2:.2f}")

elif delta < 0:
    print(f"As duas raízes são complexas e diferentes, onde: x₁ = {strComplex(x1, nDigits = 2)} e x₂ = {strComplex(x2, nDigits = 2)}i")

