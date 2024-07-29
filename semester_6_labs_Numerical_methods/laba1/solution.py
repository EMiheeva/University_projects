'''
Построение таблиц
'''
import numpy as np
import matplotlib.pyplot as plt

a = 1
b = 2
n = 10
h = (b-a)/n

x = np.arange(a, b, h)
y = -2 * np.exp(-x) + x / 2
y = np.round(y, 7)

fig, ax = plt.subplots()
ax.axis('off')
ax.table(cellText=np.column_stack((x,y)), colLabels=['x', 'y = f(x)'], loc='center')

plt.show()
