import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq
plt.figure(figsize=(9,9))
x = np.linspace(-5,5,1000)
X = np.array([0.,1., 2., 3., -1., -2.,-3.])
Y = np.array([-1.22, 1.85, 3.22, 10.29, 2.21,3.72,8.7])
def f(p):
    a, b,c = p
    return(Y-(a*X*X+b*X+c))
r = leastsq(f, [1,0,0])
a, b,c = r[0]
print("k=",a,"b=",b,"c=",c)
plt.scatter(X,Y, s=100, alpha=1.0, marker='o',label=u'data point')
y=a*x*x+b*x+c
ax = plt.gca()

ax.set_xlabel(..., fontsize=20)
ax.set_ylabel(..., fontsize=20)
#设置坐标轴标签字体大小

plt.plot(x, y, color='r',linewidth=5, linestyle=":",markersize=20, label=u'Fitting curve')

plt.legend(loc=0, numpoints=1)
leg = plt.gca().get_legend()
ltext  = leg.get_texts()
plt.setp(ltext, fontsize='xx-large')

plt.xlabel(u'ampere/A')
plt.ylabel(u'volt/V')

plt.xlim(x.min()*1.1, x.max() * 1.1)
plt.ylim(-2, y.max() * 1.1)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
#刻度字体大小
plt.legend(loc='upper left')

plt.show()
