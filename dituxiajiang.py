from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d
figure = plt.figure()
#ax = Axes3D(figure)
ax = figure.gca(projection="3d")
x1 = np.linspace(-6, 6, 1000)
y1 = np.linspace(-6, 6, 1000)
x, y = np.meshgrid(x1, y1)
z = (x**2+y-11)**2+(x+y**2-7)**2
# ax.plot_surface(x,y,z,rstride=10,cstride=4,cmap=cm.YlGnBu_r)
ax.plot_surface(x, y, z, cmap="rainbow")
plt.show()

# 梯度下降法寻找2D函数最优值函数


def f(x):
    return (x[0]**2+x[1]-11)**2+(x[0]+x[1]**2-7)**2


x = torch.tensor([-4., 0.], requires_grad=True)
optimizer = torch.optim.Adam([x], lr=1e-3)
for step in range(20000):
    pre = f(x)
    optimizer.zero_grad()
    pre.backward()
    optimizer.step()
    if step % 2000 == 0:
        print(step, x.tolist(), pre)
