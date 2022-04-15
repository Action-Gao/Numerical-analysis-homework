import numpy as np
import SolveLine as sl

A=np.array([
[10.0,1.0,2.0,3.0,4.0],
[1.0,9.0,-1.0,2.0,-3.0],
[2.0,-1.0,7.0,3.0,-5.0],
[3.0,2.0,3.0,12.0,-1.0],
[4.0,-3.0,-5.0,-1.0,15.0]])
b=np.array([12.0,-27.0,14.0,-17.0,12.0])
x0=[0,0,0,0,0]

print('final result',sl.Jacobi(A,b,x0,100,0.0001))
print('final result',sl.GaussSeidel(A,b,x0,100,0.0001))
print('final result',sl.ConjuateGradient(A,b,x0,0.0001))