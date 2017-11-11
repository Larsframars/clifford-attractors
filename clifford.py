import matplotlib.pyplot as plt
import numpy
import random

iterations = 10000000

a =  1.8941858544848227
b =  1.8469360755704156
c =  0.05474931996943733
d =  1.0829474534934094

x = 0.0
y = 0.0
xs = []
ys = []

for step in range(iterations):    
    x_ = numpy.sin(a*y) + c*numpy.cos(a*x)
    y = numpy.sin(b*x) + d*numpy.cos(b*y)
    
    x = x_
    
    xs.append(x)
    ys.append(y)


plt.plot(xs, ys, "k,", alpha=0.1)
plt.savefig('clifford.png', format='png', dpi=500)
plt.show()


