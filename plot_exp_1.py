import matplotlib.pyplot as plt 
import numpy as np

# @title Stright Line Parameters
m = 0.0  # @param {type:"number"}

x = np.linspace(0, 2500, 2500)
y = m * x + 275

plt.plot(x, y, '-r')
plt.xlim(0, 2500)
plt.ylim(0, 400)

plt.xlabel('Size in $feet^2$')
plt.ylabel('Price in 1000\'s')
plt.title('Housing price prediction.')
plt.grid()
plt.show()
