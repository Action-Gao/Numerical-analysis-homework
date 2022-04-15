# _*_ coding: UTF-8 _*_
## 基本迭代法求解线性方程

import numpy as np

## 雅可比迭代
## 输入系数矩阵，值矩阵，最大迭代次数，精度
def Jacobi(A,b,x0,n,c):
    print('Jacobi')
    # 初始化起始向量x
    #x0=np.zeros(len(A))
    #x0=np.array([1,1,1,1])
    count = 1
    while count < n:
        nx=np.empty(len(A))
        for i in range(len(A)):
            temp=0
            for j in range(len(A)):
                if i != j:
                    temp += A[i][j]*x0[j]
            nx[i]=(b[i]-temp)/A[i][i]
        nc = np.linalg.norm(nx,np.inf)-np.linalg.norm(x0,np.inf)
        print("iteration:",count,"result:", np.around(nx,4),"error:",nc)
        if abs(nc) < c:
            return nx
        count += 1
        x0=nx
    print('达到最大迭代次数')
    return False

## 高斯赛德勒迭代
def GaussSeidel(A,b,x0,n,c):
    print('GaussSeidel')
    # 初始化起始向量x
    #x0=np.zeros(len(A))
    count = 1
    while count < n:
        nx=np.empty(len(A))
        for i in range(len(A)):
            temp=0
            tempx=x0.copy()
            for j in range(len(A)):
                if i != j:
                    temp += A[i][j]*x0[j]
            nx[i]=(b[i]-temp)/A[i][i]
            x0[i]=nx[i]
        nc = np.linalg.norm(nx)-np.linalg.norm(tempx)
        print("iteration:",count,"result:", np.around(nx,4),"error:",nc)
        if abs(nc) < c:
            return nx
        count += 1
        x0=nx
    print('Reaches the maximum number of iterations')
    return False   

## 松弛迭代法（SOR）
def SOR(A,b,x0,n,c,w):
    print('SOR')
    # 初始化起始向量x
    #x0=np.zeros(len(A))
    count = 1
    while count < n:
        nx=np.empty(len(A))
        for i in range(len(A)):
            temp=0
            tempx=x0.copy()
            for j in range(len(A)):
                if i != j:
                    temp += A[i][j]*x0[j]
            nx[i]=(1-w)*x0[i]+w*(b[i]-temp)/A[i][i]
            x0[i]=nx[i]
        nc = np.linalg.norm(nx)-np.linalg.norm(tempx)
        print("iteration:",count,"result:", np.around(nx,4),"error:",nc,w)
        if abs(nc) < c:
            return nx
        count += 1
    print('Reaches the maximum number of iterations')
    return False     

## 共轭梯度法
def ConjuateGradient(A,b,x,c):
    print('ConjuateGradient')
    #x=np.zeros(len(A)) # 初始值x0
    r=b-np.dot(A,x)
    p=r  #p0=r0

    for i in range(len(A)):
        r1=r
        a=np.dot(r.T,r)/np.dot(p.T,np.dot(A,p))
        x = x + a * p    #x(k+1)=x(k)+a(k)*p(k)
        r=b-np.dot(A,x)  #r(k+1)=b-A*x(k+1)
        q = np.linalg.norm(np.dot(A, x) - b) / np.linalg.norm(b)
        print('iteration:', i,'result',x,'error',q)
        if q<c:
            break
        else:
            beta=np.linalg.norm(r)**2/np.linalg.norm(r1)**2
            p=r+beta*p  #p(k+1)=r(k+1)+beta(k)*p(k)
    return x
