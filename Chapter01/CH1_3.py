import matplotlib.pyplot as plt
import numpy as np
import math
def PlotY(x_list,n):
    Y=[]
    for t in x_list:
        y_sum = 0
        for i in range(0,n+1):
            y_sum += (math.pow(-1,i))*((math.pow(t,2*i+1))/(math.factorial(2*i+1)))
        #print(y_sum)
        Y.append(y_sum)
    #plt.plot(x_list,Y)
    return Y

x=list(np.linspace(0,6.5,100))
##绘制sinx
y1=[math.sin(t) for t in x]
plt.plot(x,y1,label='y1,sinx',color='r',linestyle='-')
##绘制n=2
y2 = PlotY(x,2)
plt.plot(x,y2,label='y2,n=2',color='b',linestyle='--')
##绘制n=5
y3 = PlotY(x,5)
plt.plot(x,y3,label='y3,n=5',color='g',linestyle='-.')
##绘制n=10
y4 = PlotY(x,10)
plt.plot(x,y4,label='y4,n=10',color='k',linestyle=':')
##设置xy轴
plt.legend(loc=0,ncol=1)                                                       # 指定图例位置，1右上角，2左上角，3右下角，4左下角，0自动适应图像
plt.xticks(fontsize= 13, fontfamily= "Times New Roman")                        # x 轴刻度字体大小，字体类型
plt.yticks(fontsize= 13, fontfamily= "Times New Roman")                        # y 轴刻度字体大小，字体类型
plt.tick_params(direction= "in", width= 2.0, length= 5.0)                      # 刻度显示在绘图区域内侧，宽度2.0，高度5.0
plt.axhline(y=plt.ylim()[0], xmin= 0.0, color= "k", linewidth= 2.0)            # 加粗显示 x 轴
plt.axvline(x=plt.xlim()[0], ymin= 0.0, color= "k", linewidth= 2.0)            # 加粗显示 y 轴
plt.xlabel(xlabel='X', fontsize= 18, fontfamily= "Times New Roman")            # x轴名称及字号字体
plt.ylabel(ylabel='Y', fontsize= 18, fontfamily= "Times New Roman")            # y轴名称及字号字体
##展示图像
plt.show()
