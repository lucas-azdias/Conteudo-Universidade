import matplotlib.pyplot as pyplot
import matplotlib.widgets as widgets
import mpl_interactions.ipyplot as ipyplot
# import numpy as np
import json

# Classes
class Line:
  def __init__(self, a=0, b=0):
    self.a = a
    self.b = b
  
  def solve(self, x): # Retorna y para um dado valor de x
    return x * self.a + self.b

  @staticmethod
  def intersect_lines(line1, line2): # Retorna o ponto de intersecção de duas linhas
    if (line1.a - line2.a) != 0:
      x = (line2.b - line1.b) / (line1.a - line2.a)
      y = line1.solve(x)
      return (x, y)
    else:
      return None

  @staticmethod
  def reverse_line(line): # Inverte a linha
    return Line(1 / line.a, -line.b / line.a)

# Functions
@staticmethod
def import_json(name): # Importa um json como um objeto
  with open(f"{name}.json", "r", encoding="utf") as file:
    config = json.load(file)
  return config

@staticmethod
def get_offset(val, offset_ratio):  # Determina o offset em unidades absolutas para uma dada porcentagem de um valor
  return abs(val) * offset_ratio

@staticmethod
def add_offset(val, offset): # Adiciona um offset a um dado valor
  return val + offset

@staticmethod
def equilibrio(o, d): # Retorna o ponto de equilíbrio para a oferta e para a demanda
  point = Line.intersect_lines(o, d)
  return (point[1], point[0])

@staticmethod
def cria_gráfico(o, d, eq, offset_ratio=0): # Cria um gráfico para a oferta e para a demanda com um dado offset
  pyplot.figure(CONFIG["graph"]["window_title"])
  pyplot.title(CONFIG["graph"]["graph_title"])
  pyplot.xlabel(CONFIG["graph"]["xlabel"])
  pyplot.ylabel(CONFIG["graph"]["ylabel"])

  o = Line.reverse_line(o)  # Inverte a função de oferta
  d = Line.reverse_line(d)  # Inverte a função de demanda

  x = [eq[0] / 2, 3 * eq[0] / 2]  # Define as fronteiras no eixo x
  yo = [o.solve(x[0]), o.solve(x[1])] # Define as fronteiras no eixo y de oferta
  yd = [d.solve(x[0]), d.solve(x[1])] # Define as fronteiras no eixo y de demanda

  # Determina os offsets unitários para os eixos
  xoff = get_offset(min(x), offset_ratio)
  yoff = get_offset(min(yo + yd), offset_ratio)

  # Define os limites das fronteiras do gráfico
  axis_lim = [add_offset(min(x), -xoff), add_offset(max(x), xoff), add_offset(min(yo + yd), -yoff), add_offset(max(yo + yd), yoff)]
  pyplot.axis(axis_lim)

  # Define se haverá uma grade
  pyplot.grid(CONFIG["graph"]["has_grid"])

  # Coloca curvas de demanda e de oferta no gráfico
  pyplot.plot([x[0], x[1]], [yo[0], yo[1]], color=CONFIG["o"]["color"], zorder=CONFIG["o"]["zorder"], label=CONFIG["o"]["label"])  # Oferta
  pyplot.plot([x[0], x[1]], [yd[0], yd[1]], color=CONFIG["d"]["color"], zorder=CONFIG["d"]["zorder"], label=CONFIG["d"]["label"])  # Demanda

  # Coloca ponto no gráfico
  pyplot.scatter(eq[0], eq[1], color=CONFIG["eq"]["color"], zorder=CONFIG["eq"]["zorder"], label=CONFIG["eq"]["label"]) # Equilíbrio

  if CONFIG["graph"]["has_legend"]:
    pyplot.legend() # Constrói a legenda
  pyplot.show() # Constrói a janela com o que foi dado

# Head
CONFIG = import_json("config") # Importa as configurações do programa
headers = import_json("headers") # Importa os dados iniciais para o programa

# Body
o = Line(headers["o"]["a"], headers["o"]["b"]) # Pega as constantes da reta de oferta
d = Line(headers["d"]["a"], headers["d"]["b"]) # Pega as constantes da reta de demanda

offset_ratio = headers["offset_ratio"]  # Pega o percentual de offset

cria_gráfico(o, d, equilibrio(o, d), offset_ratio)

#1. Criar maneira de limitar fronteiras do gráfico e as linhas das funções
#   aos valores positivos de quantidade (pois preços negativos existem, sendo
#   exemplos: lixo e petróleo na pandemia; porém quantidades negativas não
#   são úteis para uma análise).

#   Links:
#     https://en.wikipedia.org/wiki/Negative_pricing
#     https://www.desmos.com/calculator/esk9xdt7xn (sugestão de como converter o equilíbrio para um positivo)

#2. Usar widgets para criar sliders para os gráficos de oferta e de demanda
#   para variar de acordo com as variáveis postas pelo professor.

#   Links:
#     https://matplotlib.org/stable/gallery/widgets/slider_demo.html
#     https://calc-again.readthedocs.io/en/latest/calc_notebooks/0.12_calc_consumer_surplus.html
#     https://www.youtube.com/watch?v=N8pl74Kk30c&ab_channel=JieJenn

#   Variáveis para variação da demanda:
#     1. Renda.
#     2. Preço dos bens relacionados: bens substitutos X bens complementares.
#     3. Gostos.
#     4. Expectativas.
#     5. Número de compradores.

#   Variáveis para variação da oferta:
#     1. Preço dos insumos.
#     2. Tecnologia.
#     3. Expectativas.
#     4. Número de vendedores.
