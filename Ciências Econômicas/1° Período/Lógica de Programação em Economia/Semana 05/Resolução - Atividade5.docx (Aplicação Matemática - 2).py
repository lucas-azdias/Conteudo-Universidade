print("\n| Cálculo do IMC de uma pessoa |\n")

#Head
mass = float(input("Peso da pessoa: "))
height = float(input("Altura da pessoa: "))

imc = 0
result = "Resultado: A pessoa está "

#Body
imc = mass / (height ** 2)

if imc < 18.5:
    result += "abaixo do peso ideal"
elif 18.5 < imc < 25:
    result += "no peso ideal"
elif 25 < imc < 30:
    result += "com sobrepeso"
elif 30 < imc < 35:
    result += "com obesidade de grau 1"
elif 35 < imc < 40:
    result += "com obesidade de grau 2"
elif imc > 40:
    result += "com obesidade mórbida (de grau 3)"

result += f", sendo seu IMC igual a {imc:.2f}"

print(result)