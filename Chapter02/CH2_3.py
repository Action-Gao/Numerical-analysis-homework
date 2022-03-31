## 方程组的性态和矩阵条件数的实验

from typing import Type
import numpy as np

def set_A_matrix(n,cho):
    A0 = np.empty((n,n))
    A1 = np.empty((n,n))
    for i in range(0,n):
        for j in range(0,n):
            A0[i,j]=(1+0.1*(i+1))**((j+1)-1)
            A1[i,j]=1/((i+j+2)-1)

    if cho == 0:
        return A0
    elif cho == 1:
        return A1

def set_B_matrix(n,A):
    B = np.empty(n)
    for i in range(0,n):
        sumA = 0
        for j in range(0,n):
            sumA = sumA + A[i][j]
        B[i] = sumA
    return B

n=10
A0=set_A_matrix(n,0)
B0=set_B_matrix(n,A0)
A0[2,2]=A0[2,2]+(10E-8)
A0[-1,-1]=A0[-1,-1]+(10E-8)
cond_A0=np.linalg.cond(A0,2)
X0=np.linalg.solve(A0,B0)
print('n=%d'%n)
print(np.around(X0,4))
A1=set_A_matrix(n,1)
B1=set_B_matrix(n,A1)
A1[2,2]=A1[2,2]+(10E-8)
A1[-1,-1]=A1[-1,-1]+(10E-8)
cond_A1=np.linalg.cond(A1,2)
X1=np.linalg.solve(A1,B1)
print('n=%d'%n)
print(np.around(X1,4))
