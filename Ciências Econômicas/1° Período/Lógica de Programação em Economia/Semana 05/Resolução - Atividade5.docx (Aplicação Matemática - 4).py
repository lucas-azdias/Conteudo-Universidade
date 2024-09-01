print("\n| Determinador do tipo de triângulo quanto aos lados |\n")

#Head
a = float(input("Valor do lado a: "))
b = float(input("Valor do lado b: "))
c = float(input("Valor do lado c: "))

#Body
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("\nOs valores para os lados formam um triângulo equilátero")
    elif a == b  or a == c or b == c:
        print("\nOs valores para os lados formam um triângulo isósceles")
    else:
        print("\nOs valores para os lados formam um triângulo escaleno")
else:
    print("\nOs valores para os lados não conseguem formar um triângulo")