'''
Метод Адамса 3-го порядка
'''
import numpy as np
from tabulate import tabulate
def y_double_diff(x, y):
    return np.cos(1.5 * x + y)

y_0 = 0
inaccuracy = 0.001
a = 0
b = 0.5
n = 40
h = (b - a) / n
order = 3

x = [a + i * h for i in range(n + 1)]
y = [0 for i in range (n + 1)]
g = [1 for i in range (n + 1)]

for i in range(n):
    if i < order:
        g[i + 1] = g[i] + h * y_double_diff(x[i], y[i])
        y[i + 1] = y[i] + h * g[i]
    else:
        g[i + 1] = g[i] + h * (23 * y_double_diff(x[i], y[i]) - 16 * y_double_diff(x[i - 1], y[i - 1]) + 5 * y_double_diff(x[i - 2], y[i - 2])) / 12
        y[i + 1] = y[i] + h * (23 * g[i] - 16 * g[i - 1] + 5 * g[i - 2]) / 12

flag_for_error = True
while flag_for_error:
    n *= 2
    h /= 2
    X = [a + i * h for i in range(n + 1)]
    G = [1 if i == 0 else 0 for i in range(n + 1)]
    Y = [0 for i in range(n + 1)]
    for i in range(n):
        if i < order:
            G[i + 1] = G[i] + h * y_double_diff(X[i], Y[i])
            Y[i + 1] = Y[i] + h * G[i]
        else:
            G[i + 1] = G[i] + h * (23 * y_double_diff(X[i], Y[i]) - 16 * y_double_diff(X[i - 1], Y[i - 1]) + 5 * y_double_diff(X[i - 2], Y[i - 2])) / 12
            Y[i + 1] = Y[i] + h * (23 * G[i] - 16 * G[i - 1] + 5 * G[i - 2]) / 12
    flag_for_error = False

    for i in range(len(y)):
        if abs(Y[i * 2] - y[i]) > inaccuracy:
            flag_for_error = True
    x = X
    y = Y

x_answer = [round(i, 3) for i in X]
y_answer = [round(i, 3) for i in Y]

print("Метод Адамса 3-го порядка")
head_for_table = ["k-точка разбиения", "x_k", "y_k"]
data_result = []
print(f"n = {n} \nh = {h}")
for i in range(len(x_answer)):
    data_result.append([i, x_answer[i], y_answer[i]])
print(f"Итоговое количество точек разбиения: {len(data_result)}")
print(tabulate(data_result, headers=head_for_table, tablefmt='fancy_grid', floatfmt=".3f", numalign="center"))
