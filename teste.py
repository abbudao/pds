import numpy
import matplotlib.pyplot as plt
import math
def chebyshev(x,n):
    if(math.fabs(x)<1):
        return(math.cos(n*math.acos(x)))
    elif(x>=1):
        return(math.cosh(n*math.acosh(x)))
    else:
        return(math.pow(-1,n)*math.cosh(n*math.acosh(-1*x)))
#from sympy import *
#init_printing()
x = numpy.arange(0, 2, 0.01)
for i in range(5):
    plt.plot(x, x**i)
plt.show()

y = numpy.arange(0, 2, 0.01)
print(chebyshev(0.11,2))
for i in range(1,5):
    a=[chebyshev(y,i) for y in numpy.arange(0.1,2,0.01)]
    plot.plot(a)
plt.show()
