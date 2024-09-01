"""Lucas Azevedo Dias"""
print("\n| PjBL - Calculador de valor futuro líquido do fluxo de caixa |\n")

#Head
custo = float(input("Capital inicial investido: ")) #Define o capital inicial utilizado
i = float(input("Taxa de juros: ").replace(",", ".")) #Define a taxa de juros para corrigir o fluxo de caixa
t = int(input("Número de períodos do fluxo de caixa: ")) #Define o número de périodos no fluxo de caixa
caixa = list() #Cria uma lista para armazenar o fluxo de caixa
for p in range(t): #Define o fluxo de caixa de acordo com o número de períodos dado
    caixa.append(float(input(f"Entrada no caixa no período {p + 1}: ")))

fvl = 0 #Cria uma variável para armazenar o valor futuro líquido

#Body
for p in range(t): #Corrige o fluxo de caixa para o valor futuro e adiciona à variável do valor futuro líquido
    fvl += caixa[p] * (1 + i) ** (t - p - 1)

fvl -= custo * (1 + i) ** t #Retira o valor do capital inicial utilizado (corrigido pela taxa de juros) do valor futuro líquido

print(f"\nO valor futuro líquido do fluxo de caixa é: {fvl:.2f}") #Apresenta o valor futuro líquido resultante dos cálculos
if fvl > 0:
    print(f"Pelo valor futuro líquido ser maior do que 0, então houve acúmulo de capital no fluxo de caixa dada a taxa de juros de {i * 100:.1f}%\n") #Pois fvl > 0
elif fvl == 0:
    print(f"Pelo valor futuro líquido ser igual a 0, então não houve acúmulo nem perda de capital no fluxo de caixa dada a taxa de juros de {i * 100:.1f}%\n") #Pois fvl = 0
elif fvl < 0:
    print(f"Pelo valor futuro líquido ser menor do que 0, então houve perda de capital no fluxo de caixa dada a taxa de juros de {i * 100:.1f}%\n") #Pois fvl < 0
