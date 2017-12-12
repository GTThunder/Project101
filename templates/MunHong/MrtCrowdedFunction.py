import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt
y = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]


df = DataFrame(abs(np.random.randn(7, 44)), index=y, columns=x)

plt.pcolor(df)
plt.yticks(np.arange(0.5, len(df.index), 1), df.index)
plt.xticks(np.arange(0.5, len(df.columns), 1), df.columns)
plt.show()

#print('Yellow = Occupied')
#print('Purple = Vacant')
