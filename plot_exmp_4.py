import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([480, 2350])
y1 = np.array([92, 372.5])

plt.plot(x1, y1, 'o', color='black')

m = (y1[1] - y1[0]) / (x1[1] - x1[0])
b = y1[1] - m * x1[1]

x2 = np.linspace(0, 2500, 2500)
y2 = m * x2 + b

plt.plot(x2, y2, '-r')
plt.xlim(0, 2500)
plt.ylim(0, 400)

plt.xlabel('Size in $feet^2$')
plt.ylabel('Price in 1000\'s')
plt.title('Housing price predicion.')

plt.grid()
plt.show()
