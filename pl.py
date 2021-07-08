import numpy as np
import cmath
import matplotlib as mlt

a = 1
b = -7
c = 12
d = (b**2) - (4*a*c)
x1 = (-b + cmath.sqrt(d)) / (2 * a)
x2 = (-b - cmath.sqrt(d)) / (2 * a)
print(np.linspace(x1,x2,100))

x_plot = [x1, x2, 0]
y_plot = [0,0,c]
i = 0
for i in x_plot:
    j = int(x_plot[i])
print(j)    