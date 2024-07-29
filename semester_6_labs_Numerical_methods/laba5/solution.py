'''
Метод Эйлера 2-го порядка
'''
import numpy as np
from tabulate import tabulate

def euler(y_diff, y_initial, a_b_section, h, inaccuracy):
    def euler_second_step(y_diff, y_initial, x, h):
        y_part = y_initial + 0.5 * h * y_diff(x, y_initial)
        y_next = y_initial + h * y_diff(x + 0.5 * h, y_part)
        return y_next

    points_result = []

    x_0 = a_b_section[0]
    y_0 = y_initial

    points_result.append((x_0, y_0))

    while x_0 < a_b_section[1]:
        y_previous = y_0
        y_0 = euler_second_step(y_diff, y_0, x_0, h)
        x_0 += h

        points_result.append((x_0, y_0))

        if abs(y_0 - y_previous) < inaccuracy:
            break

    return points_result

def y_diff(x, y):
    return np.sin(2 * x + y) - 0.3 * y

y_initial = 0

a_b_section = [0, 0.5]
n = 8
h = (a_b_section[1] - a_b_section[0]) / n
inaccuracy = 0.001

solution = euler(y_diff, y_initial, a_b_section, h, inaccuracy)

head_for_table = ["k-точка разбиения", "x_k", "y_k"]
data_result = []

print("Метод Эйлера 2-го порядка")
print(f"n = {n} \nh = {h}")
for k, (x, y) in enumerate(solution):
    data_result.append([k, x, y])
print(f"Итоговое количество точек разбиения: {len(data_result)}")
print(tabulate(data_result, headers=head_for_table, tablefmt='fancy_grid', floatfmt=".3f", numalign="center"))
