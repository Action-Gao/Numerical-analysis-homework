import numpy as np
import SolveLine as sl

n=int(10e3)
A=np.empty([n,n])
for i in range(0,n):    
    for j in range(0,n):
        A[i][j]=0
        if i==j:
            A[i][j]=2.0
        elif abs(i-j)==1:
            A[i][j]=-1.0
        elif (i+j==n-1)and(i != (n-1)/2)and(i != ((n-1)/2)+1):
            A[i][j]=0.5
        else:
            A[i][j]=0.0

b=np.empty(n)
for i in range(0,n):
    if i==0 or i==n-1:
        b[i]=2.5
    elif i==int((n-1)/2) or i==int((n-1)/2)+1:
        b[i]=1.0
    else:
        b[i]=1.5
x0=np.zeros(n)
print(A)
print(b)
print('final result',sl.ConjuateGradient(A,b,x0,0.0001))