import math
import matplotlib.pyplot as plt
import numpy
import random

a =  -1.5960972779713606
b =  1.4975440895690856
c =  0.9985838244580214
d =  0.20799250263985192

for frame in range(30):
    number = frame
    x = 0.0
    y = 0.0
    xpoints = []
    ypoints = []

    for step in range(100000):

        x_ = numpy.sin(a*y) + c*numpy.cos(a*x)
        y = numpy.sin(b*x) + d*numpy.cos(b*y)
        
        x = x_
        
        xpoints.append(x)
        ypoints.append(y)

    fig = plt.figure()
    plt.plot(xpoints, ypoints, "k,", alpha=0.1)
    plt.savefig(str(frame)+'.png', format='png', dpi=200, facecolor='k')
    
    a += 0.1/30



