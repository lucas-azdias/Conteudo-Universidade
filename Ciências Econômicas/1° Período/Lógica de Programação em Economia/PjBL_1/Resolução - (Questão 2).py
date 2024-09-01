"""Lucas Azevedo Dias"""
print("\n| PjBL - Calculador de valor presente líquido do fluxo de caixa |\n")

#Head
custo = float(input("Capital inicial investido: ")) #Define o capital inicial utilizado
i = float(input("Taxa de juros: ").replace(",", ".")) #Define a taxa de juros para corrigir o fluxo de caixa
t = int(input("Número de períodos do fluxo de caixa: ")) #Define o número de périodos no fluxo de caixa
caixa = list() #Cria uma lista para armazenar o fluxo de caixa
for p in range(t): #Define o fluxo de caixa de acordo com o número de períodos dado
    caixa.append(float(input(f"Entrada no caixa no período {p + 1}: ")))

pvl = 0 #Cria uma variável para armazenar o valor presente líquido

#Body
for p in range(t): #Corrige o fluxo de caixa para o valor presente e adiciona à variável do valor presente líquido
    pvl += caixa[p] / (1 + i) ** (p + 1)

pvl -= custo #Retira o valor do capital inicial utilizado (que não precisa ser corrigido) do valor presente líquido

print(f"\nO valor presente líquido do fluxo de caixa é: {pvl:.2f}") #Apresenta o valor presente líquido resultante dos cálculos
if pvl > 0:
    print(f"Pelo valor presente líquido ser maior do que 0, então houve acúmulo de capital no fluxo de caixa dada a taxa de juros de {i * 100:.1f}%\n") #Pois pvl > 0
elif pvl == 0:
    print(f"Pelo valor presente líquido ser igual a 0, então não houve acúmulo nem perda de capital no fluxo de caixa dada a taxa de juros de {i * 100:.1f}%\n") #Pois pvl = 0
elif pvl < 0:
    print(f"Pelo valor presente líquido ser menor do que 0, então houve perda de capital no fluxo de caixa dada a taxa de juros de {i * 100:.1f}%\n") #Pois pvl < 0
