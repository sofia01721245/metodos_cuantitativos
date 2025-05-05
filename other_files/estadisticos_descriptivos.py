import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.random.normal(0, 1, 500)

data2 = np.random.normal(1, 1, 500)


data3 = np.random.normal(0, 2, 500)


#Show all three histograms in one plot
plt.hist(data, bins=30, density=True, alpha=0.6, color='g', label='Mean 0, Variance 1')
plt.hist(data2, bins=30, density=True, alpha=0.6, color='b', label='Mean 1, Variance 1')
plt.hist(data3, bins=30, density=True, alpha=0.6, color='r', label='Mean 0, Variance 2')
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Histograms of Normally Distributed Data')
plt.legend()
plt.show()

