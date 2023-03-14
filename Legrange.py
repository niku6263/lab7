import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

def lagrange(xeval,xint,yint,N):

    lj = np.ones(N+1)
    
    for count in range(N+1):
       for jj in range(N+1):
           if (jj != count):
              lj[count] = lj[count]*(xeval - xint[jj])/(xint[count]-xint[jj])

    yeval = 0.
    
    for jj in range(N+1):
       yeval = yeval + yint[jj]*lj[jj]
  
    return(yeval)

f = lambda x: 1/(1+(10*x)**2)

N = 11
''' interval'''
a = -1
b = 1
   
   
''' create equispaced interpolation nodes'''
xint = np.linspace(a,b,N+1)
    
''' create interpolation data'''
yint = f(xint)
    
''' create points for evaluating the Lagrange interpolating polynomial'''
Neval = 1000
xeval = np.linspace(a,b,Neval+1)
yeval_l= np.zeros(Neval+1)
yeval_dd = np.zeros(Neval+1)
  
'''Initialize and populate the first columns of the 
 divided difference matrix. We will pass the x vector'''
y = np.zeros( (N+1, N+1) )
     
for j in range(N+1):
    y[j][0]  = yint[j]

''' evaluate lagrange poly '''
for kk in range(Neval+1):
    yeval_l[kk] = lagrange(xeval[kk],xint,yint,N)
          

    


''' create vector with exact values'''
fex = f(xeval)
       

plt.figure()    
plt.plot(xeval,fex,'ro-', label="f(x)")
plt.plot(xeval,yeval_l,'bs--', label="p(x)") 
plt.title("Lagrange N=11")
plt.legend()

plt.figure() 
err_l = abs(yeval_l-fex)
plt.semilogy(xeval,err_l,'ro--',label='lagrange')
plt.title("Lagrange Error")
plt.legend()
plt.show()