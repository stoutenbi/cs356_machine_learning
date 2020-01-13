import matplotlib.pyplot as plt 
import numpy as np

# @title Straight Line Parameters
b = 100  # @param {type:"number"}
x = np.linspace(0, 2500, 2500)
y = np.ones(2500) * b

plt.plot(x, y, '-r')
plt.xlim(0, 2500)
plt.ylim(0, 400)

plt.xlabel('Size in $feet^2$')
plt.ylabel('Price in 1000\'s')
plt.title('Housing price predicion.')

plt.grid()
plt.show()
