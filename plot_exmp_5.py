import matplotlib.pyplot as plt
import numpy as np

x = np.array([480, 510, 520, 850, 960, 1200, 1400, 1650, 1700, 1920, 2350])
y = np.array([98, 110, 200, 210, 280, 265, 300, 287, 325, 300, 290])

plt.plot(x, y, 'o', color='black')

m = 0.07
b = 150

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
