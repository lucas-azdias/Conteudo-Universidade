"""
Considere o modelo básico de determinação de renda em uma economia fechada:

Consumo = C0 + c.Y
Investimento = I0
Gasto do Governo = G0

Onde:

Y é a renda ou PIB
C0 é o consumo autônomo. C0 representa as influências psicológicas sobre o consumo
c é a propensão marginal a consumir que deve satisfazer a seguinte condição 0 < c < 1
I0 é o investimento autônomo. I0 representa a influência das expectativas empresariais sobre o investimento
G0 é o gasto do governo autônomo, ou seja, que independe da renda

Construa um algoritmo que retorne o PIB e o multiplicador keynesiano
"""

# cálculo do valor do PIB
c0 = float(input('Digite o valor do consumo autônomo: '))
i0 = float(input('Digite o valor do investimento autônomo: '))
g0 = float(input('Digite o valor do gasto do governo: '))
c = float(input('Digite o valor da propensão marginal a consumir: '))

# cálculo do valor do multiplicador keynesiano
alpha = 1 / (1 - c)

# cálculo das variáveis autônomas
A = c0 + i0 + g0

# cálculo do PIB
y = alpha * A
print('O PIB desta economia é de ', y)


