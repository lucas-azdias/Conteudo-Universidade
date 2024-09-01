"""
Calcule uma média aritmética que receba como entradas as quatro notas bimestrais e, por sua vez,
retorne a situação do estudante ao final do semestre de acordo com a tabela abaixo.

Média Final	Situação do Estudante
Nota maior ou igual a 7.0 >>>> Aprovado
Nota entre 4.0 (inclusive) e 7.0 >>> Recuperação
Nota menor do que 4.0 >>> Reprovado
"""
# cálculo da média aritimética a partir de dados de entrada (problema mutamente exclusivo)
n1 = float(input('Digite o valor da primeira nota: '))
n2 = float(input('Digite o valor da segunda nota: '))  # typecast
n3 = float(input('Digite o valor da terceira nota: '))
n4 = float(input('Digite o valor da quarta nota: '))

# fórmula da média aritmética
media = (n1 + n2 + n3 + n4) / 4
print('A média semestral foi de ', media)

if media >= 7:
    print('O estudante está aprovado')
elif 4 <= media < 7:
    print('O estudante está em recuperação')
else:
    print('O estudante está reprovado')

