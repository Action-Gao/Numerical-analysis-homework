# 求解三维线性方程组
# Gauss消去法计算线性方程组
## 输入系数A和b
A=[[1,1,1],
   [12,-3,3],
   [-18,3,-1]]
b=[6,15,-15]
x=b[:]  ## 用来存储结果
k=0
n=len(A)  ## 方程维数

## 消元
for k in range(0,n-1):
    if A[k][k] == 0:
        print('error,Akk = 0')
        exit(0)
    ## 列主元素法
    ## 寻找最大的行
    temp = abs(A[k][k])
    for ci in range(k,n):
        A_cik = abs(A[ci][k])
        if A_cik > temp:
            temp = A_cik
            max_i = ci  ## 最大行号
    ## 交换A的行
    for cj in range(k,n):
        temp_a = A[k][cj]
        A[k][cj] = A[max_i][cj]
        A[max_i][cj] = temp_a
    ## 交换b的行
    temp_b = b[k]
    b[k] = b[max_i]
    b[max_i]=temp_b

    for i in range(k+1,n):
        A[i][k] = A[i][k]/A[k][k]
        b[i] = b[i] - A[i][k]*b[k]
        for j in range(k+1,n):
            A[i][j] = A[i][j]-A[i][k]*A[k][j]

if A[n-1][n-1]==0:
    print('error,Ann=0')
    exit(0)
else:
    x[n-1]=b[n-1]/A[n-1][n-1]

## 逆推结果
for k in range(n-2,-1,-1):
    a_sum = 0
    for l in range(k+1,n):
        a_sum += x[l]*A[k][l]
    x[k] = (b[k] - a_sum)/A[k][k]

## 输出结果
print(x)