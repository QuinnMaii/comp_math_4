import numpy as np
from numpy import double
import matplotlib.pyplot as plt

print('This program takes in input, uses Lagrange polynomial to solve for polynomials')

degree = int(input('Enter the degree of the polynomial: '))

X = np.array(list(map(double,input('Enter x values x(i): ').strip().split()))[:degree +1], double)
fi = np.array(list(map(double,input('Enter functions f(i): ').strip().split()))[:degree +1], double)


print('Do you also want to know the function at a particular point x?\n'
      'Press 1 if YES, press anything if NO')
choice = int(input())

xp =0

if choice == 1:
    xp = double(input('Enter the value: '))

xc = xp
xplt = np.linspace(X[0], X[-1])
yplt = np.array([], double)

for xp in xplt:
    yp = 0
    for xi, yi in zip(X, fi):
        product = np.prod(((xp - X[X != xi])/(xi-X[X != xi])))
        yp += yi*product
    yplt = np.append(yplt, yp)


#find solution for xc
yc=0
for i in range(len(fi)):
    p=1
    for j in range(len(X)):
        if j!=i:
            p*=(xc -X[j])/(X[i] - X[j])
    yc+=fi[i]*p

print(xc, yc)
#plot
plt.plot(xc, yc, 'go')
plt.plot(X,fi, 'ro', xplt, yplt, 'b-')
plt.grid()
plt.title('Graph of f(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.show()