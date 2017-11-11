import matplotlib.pyplot as plt
import numpy
import random

iterations = 100000


def ranclifford(iterations):
    a = random.uniform(-2, 2)
    b = random.uniform(-2, 2)
    c = random.uniform(-2, 2)
    d = random.uniform(-2, 2)

    x = 0.0
    y = 0.0
    xs = []
    ys = []

    for step in range(iterations):
        if step == 10000:
            if len(set(xs)) < 10000:
                return 0, 0
        
        x_ = numpy.sin(a*y) + c*numpy.cos(a*x)
        y = numpy.sin(b*x) + d*numpy.cos(b*y)
        
        x = x_
        
        xs.append(x)
        ys.append(y)
        
    print("a = ",a)
    print("b = ",b)
    print("c = ",c)
    print("d = ",d)
    print("")
    return xs, ys
    
while True:
    xs, ys = ranclifford(iterations)
    if xs != 0:
        break

print(len(set(xs)))
print(len(set(ys)))

plt.plot(xs, ys, "k,", alpha=0.1)
plt.show()

