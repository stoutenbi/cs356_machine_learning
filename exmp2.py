import matplotlib.pyplot as plt
import numpy as np

area = np.array([480, 510, 520, 850, 960, 1200, 1400, 1650, 1700, 1920, 2350])
price = np.array([98, 110, 200, 210, 280, 265, 300, 287, 325, 300, 290])

plt.plot(area, price, 'o', color='black');

theta_1 = 0.00               # m : slope
theta_0 = np.average(price)  # b : y-intercept


x = np.linspace(0, 2500, 2500)
y = theta_1 * x + theta_0

h = theta_1 * area + theta_0

plt.plot(x, y, '-r')

plt.xlim(0, 2500)
plt.ylim(0, 400)

plt.xlabel('Size in $feet^2$')
plt.ylabel('Price in 1000\'s')
plt.title('Housing price predicion.')

plt.grid()
plt.show()



mse = np.sum((price - h)*(price - h)) / (2*11)

print()
print(mse)
