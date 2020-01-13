import matplotlib.pyplot as plt
import numpy as np
x = np.array([480, 510, 520, 850, 960, 1200, 1400, 1650, 1700, 1920, 2350])
y = np.array([92, 96.5, 98, 147.5, 164, 200, 230, 267.5, 275, 308, 372.5])
plt.plot(x, y, 'o', color='black')
m = 0.15
b = 20
s = np.linspace(0, 2500, 2500)
t = m * s + b
plt.plot(s, t, '-r')
plt.xlim(0, 2500)
plt.ylim(0, 400)
plt.xlabel('Size in $feet^2$')
plt.ylabel('Price in 1000\'s')
plt.title('Housing price predicion.')
plt.grid()
plt.show()
