'''
Метод Рунге-Кутта 4-го порядка
'''
import numpy as np
from tabulate import tabulate
def runge_kutta(y_diff, y_initial, a_b_section, h, inaccuracy):
    def runge_kutta_step(y_diff, y_initial, x, h):
        k1 = h * y_diff(x, y_initial)
        k2 = h * y_diff(x + 0.5 * h, y_initial + 0.5 * k1)
        k3 = h * y_diff(x + 0.5 * h, y_initial + 0.5 * k2)
        k4 = h * y_diff(x + h, y_initial + k3)
        delta_y = y_initial + (k1 + 2*k2 + 2*k3 + k4) / 6
        return delta_y

    points_result = []

    x_0 = a_b_section[0]
    y_0 = y_initial

    points_result.append((x_0, y_0))

    while x_0 < a_b_section[1]:
        y_prev = y_0
        y_0 = runge_kutta_step(y_diff, y_0, x_0, h)
        x_0 += h

        points_result.append((x_0, y_0))

        if abs(y_0 - y_prev) < inaccuracy:
            break

    return points_result
def y_diff(x, y):
    return np.sin(2 * x + y) - 0.3 * y

y_initial = 0
a_b_section = [0, 0.5]

n = 8
h = (a_b_section[1] - a_b_section[0]) / n
inaccuracy = 0.001

solution = runge_kutta(y_diff, y_initial, a_b_section, h, inaccuracy)

head_for_table = ["k-точка разбиения", "x_k", "y_k"]
data_result = []

print("Метод Рунге-Кутта 4-го порядка")
print(f"n = {n} \nh = {h}")
for k, (x, y) in enumerate(solution):
    data_result.append([k, x, y])
print(f"Итоговое количество точек разбиения: {len(data_result)}")
print(tabulate(data_result, headers=head_for_table, tablefmt='fancy_grid', floatfmt=".3f", numalign="center"))
