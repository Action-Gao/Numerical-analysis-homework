## 使用追赶法解三对角方程组
import numpy as np

a=[0,-2,-2,-2,-2,-2,-2,-2]
b=[2,5,5,5,5,5,5,5]
c=[-2,-2,-2,-2,-2,-2,-2]
d=[8.148,0,0,0,0,0,0,0]

for i in range(1,len(b)):
    a[i] = a[i]/b[i-1]   ## 计算l矩阵
    b[i] = b[i]-c[i-1]*a[i]   ## 计算u矩阵
    d[i] = d[i]-a[i]*d[i-1]   ## 计算y
d[-1] = d[-1]/b[-1]
for i in range(len(b)-2,-1,-1):
    d[i] = (d[i]-c[i]*d[i+1])/b[i]

print(np.round(d,4))