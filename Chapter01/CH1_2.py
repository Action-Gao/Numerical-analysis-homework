import math #导入数学库
pi = 0
i = 1
while True:
    pi += (math.pow(-1,i))*(1/(2*i-1))*(-1)
    if 1/(2*i+1) < math.pow(10,-4):
        break
    i = i+1
pi = pi*4
print(pi,i)
