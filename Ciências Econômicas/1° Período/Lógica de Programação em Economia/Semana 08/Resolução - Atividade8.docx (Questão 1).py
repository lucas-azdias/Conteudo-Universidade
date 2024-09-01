#Head
num_wines = 0
wines = {"T": 0, "B": 0, "R": 0}

#Body
while True:
    inputWine = input("Digite o tipo de vinho: ")

    if inputWine == "T" or inputWine == "t":
        print("Vinho tinto cadastrado")
        wines["T"] += 1
    elif inputWine == "B" or inputWine == "b":
        print("Vinho branco cadastrado")
        wines["B"] += 1
    elif inputWine == "R" or inputWine == "r":
        print("Vinho rosê cadastrado")
        wines["R"] += 1
    elif inputWine == "F" or inputWine == "f":
        print("Programa encerrado")
        break
    else:
        print("Valor inválido")

for wine in wines.values():
    num_wines += wine

print(f"""
Dados cadastrados
    Vinhos tintos: {wines["T"]} ({100 * wines["T"] / num_wines:.2f}%)
    Vinhos brancos: {wines["B"]} ({100 * wines["B"] / num_wines:.2f}%)
    Vinhos rosê: {wines["R"]} ({100 * wines["R"] / num_wines:.2f}%)
    Total de vinhos: {num_wines}
""")