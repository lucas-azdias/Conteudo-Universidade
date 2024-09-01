import matplotlib.pyplot as pplot
import mpl_interactions.ipyplot as iplot
import numpy as np

fig, ax = pplot.subplots()

pplot.xlabel("a")
pplot.ylabel("b")

pplot.axis([0, 100, 0, 100])

x = np.linspace(0, 100)
y = np.linspace(0, 100)

a = 1
b = 10

def func(x, a, b):
        return x * a + b

#pplot.plot(x, [func(x[0], a, b), func(x[1], a, b)])


#axes = pplot.axes([0, 100, 0, 100])
#slider = Slider(axes, label="ggg", valmin=1, valmax=2)
aslider = np.linspace(1, 100)
bslider = np.linspace(1, 1000)
iplot.plot(x, func, ax=ax, a=aslider, b=bslider)

cslider = np.linspace(1, 100)
dslider = np.linspace(1, 1000)
iplot.plot(x, func, ax=ax, a=cslider, b=dslider)

pplot.show()