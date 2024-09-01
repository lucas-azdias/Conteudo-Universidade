import matplotlib.pyplot as plt
import numpy as np


plt.style.use('seaborn-whitegrid')  # cria o grid para a plotagem do gráfico
fig = plt.figure()  # cria um objeto do tipo figure para a plotagem do gráfico
ax = plt.axes()  # cria um objeto do tipo axes para a criação dos eixos
x = np.linspace(0, 10, 1000)  # delimita a variação de valores no eixo x. Nesse caso, de 0 a 10
ax.plot(x, x)  # lê-se plot(eixo x, função que quero plotar no gráfico no eixo y)
ax.plot(x, -x + 10)  # preço = -x (quantidade demandada) + 10

plt.show()