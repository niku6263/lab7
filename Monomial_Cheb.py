import numpy as np
import matplotlib.pyplot as plt

f = lambda x: 1/(1+(10*x)**2)

N = 20
h = 2/(N-1)

x = np.zeros(N)
F = np.zeros(N)

for i in range(N):
    x[i] = np.cos(((2*(i+1) - 1)*np.pi)/(2*N))
    F[i] = f(x[i])

def monomial(x,F):
    rows = N
    cols = N
    
    V = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(N):
        for j in range(N):
            V[i][j] = x[i]**j

    invV = np.linalg.inv(V)

    c = invV@F

    return c



k = np.arange(-1,1,2/1001)
g = f(k)
p = np.zeros(len(k))
c = monomial(x,F)
for i in range(1001):
    for j in range(N):
        p[i] = p[i] + c[j]*k[i]**j

plt.plot(x,F,'o',label="f(x_j)")
plt.plot(k,p, label="p(x)")
plt.plot(k,g, label="f(x)")
plt.title("Monomial Chebechevs N=20")
plt.legend()
plt.show()