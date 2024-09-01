import matplotlib.pyplot as pplot
import ipywidgets as widgets
import numpy as np

output = widgets.Output()

with output:
    fig, ax = pplot.subplots()

pplot.xlabel("a")
pplot.ylabel("b")

pplot.axis([0, 100, 0, 100])

def func(x, a, b):
    return x * a + b

a = 1
b = 10

init = [0, 100]

x = np.linspace(init[0], init[1])
y = np.linspace(func(init[0], a, b), func(init[1], a, b))

line, = ax.plot(x, y)

#pplot.plot(x, [func(x[0], a, b), func(x[1], a, b)])

def change_a(new_a):
    return line.set_ydata(np.linspace(func(init[0], new_a, b), func(init[1], new_a, b)))

aslider = widgets.FloatSlider(
        value=a,
        min=0,
        max=20,
        description="A",
        continuous_update=False
)

aslider.observe(change_a, 'value')

controls = widgets.VBox([aslider])
widgets.HBox([controls, output])

#axes = pplot.axes([0, 100, 0, 100])
#slider = Slider(axes, label="ggg", valmin=1, valmax=2)
#slider = np.linspace(1, 100)
#bslider = np.linspace(1, 1000)
#iplot.plot(x, func, ax=ax, a=aslider, b=bslider)

#pplot.show()