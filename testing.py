from geometry import *
from matplotlib import pyplot as plt

fig = plt.figure(0)
base = Polygon.rectangle(Point(0, 0), 100, 100)
base.plot()

a = Polygon.rectangle(Point(0, 0), 50, 50)
a.plot()
b = Polygon.rectangle(Point(10, 50), 30, 40)
b.plot()
d = Polygon.rectangle(Point(50, 20), 30, 30)
d.plot()

c = a+b
c.plot()
plt.savefig("testinga.png")
