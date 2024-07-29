'''
Численное дифференцирование
'''
import numpy as np
from scipy.interpolate import lagrange
from tabulate import tabulate

a = 0.5
b = 1.5
m = 0.63
n = 5

x_k = np.linspace(a, b, n)
y_k = np.exp(x_k/2)

def derivatives(x_k, y_k, x):
    step_h = x_k[1] - x_k[0]
    i = np.searchsorted(x_k, x)
    if i > 0 and (i == len(x_k) or abs(x - x_k[i-1]) < abs(x - x_k[i])):
        i -= 1

    if i+1 < len(x_k):
        dy_left = (y_k[i + 1] - y_k[i]) / step_h
    else:
        dy_left = None

    if i-1 >= 0:
        dy_right = (y_k[i] - y_k[i-1]) / step_h
    else:
        dy_right = None


    if i-1 >= 0 and i+1 < len(x_k):
        dy2 = (y_k[i-1] - 2*y_k[i] + y_k[i+1]) / step_h**2
    else:
        dy2 = None

    return dy_left, dy_right, dy2


dy_left_k = np.array([derivatives(x_k, y_k, x)[0] for x in x_k])
dy_right_k = np.array([derivatives(x_k, y_k, x)[1] for x in x_k])
dy2_k = np.array([derivatives(x_k, y_k, x)[2] for x in x_k])

dy_exact_k = 1/2 * np.exp(x_k/2)
dy2_exact_k = 1/4 * np.exp(x_k/2)

dy_exact_m = 1/2 * np.exp(m/2)
dy2_exact_m = 1/4 * np.exp(m/2)
L = lagrange(x_k, y_k)
y_m = L(m)


head = ["x_k", "f'(x_k)_left", "f'(x_k)_center", "f'(x_k)_right", "f''(x_k)", "f'(x_k)_exact", "f''(x_k)_exact"]
main_data_result = [[], [], [], [], [], []]
for i in range(n):
    if dy_left_k[i] is not None:
        dy_left = f"{dy_left_k[i]:.4f}"
    else:
        dy_left = "None"


    if dy_right_k[i] is not None:
        dy_right = f"{dy_right_k[i]:.4f}"
    else:
        dy_right = "None"

    if dy2_k[i] is not None:
        dy2 = f"{dy2_k[i]:.4f}"
    else:
        dy2 = "None"


    if dy_left_k[i] is not None and dy_right_k[i] is not None:
        dy_center = f"{(dy_left_k[i] - dy_right_k[i]) / 2:.4f}"
    else:
        dy_center = "None"

    main_data_result[i].extend([f"{x_k[i]:.4f}", dy_right, dy_center, dy_left, dy2, f"{dy_exact_k[i]:.4f}", f"{dy2_exact_k[i]:.4f}"])


dy_left_m, dy_right_m, dy2_m = derivatives(x_k, y_k, m)

if dy_left_m is not None:
    dy_left = f"{dy_left_m:.4f}"
else:
    dy_left = "None"

if dy_right_m is not None:
    dy_right = f"{dy_right_m:.4f}"
else:
    dy_right = "None"

if dy2_m is not None:
    dy2 = f"{dy2_m:.4f}"
else:
    dy2 = "None"

if dy_left_m is not None and dy_right_m is not None:
    dy_center = f"{(dy_left_m - dy_right_m) / 2:.4f}"
else:
    dy_center = "None"

main_data_result[len(main_data_result) - 1].extend([f"{m:.4f}", dy_right, dy_center, dy_left, dy2, f"{dy_exact_m:.4f}", f"{dy2_exact_m:.4f}"])

print(tabulate(main_data_result, headers=head, tablefmt="grid"))


print(f"\nИнтерполяционный многочлен Лагранжа   L(m) = L({m}) = {round(y_m, 4)}")
print(f"Аналитическое значение функции f(m) = f({m}) = {round(np.exp(m/2), 4)}")
#print(f"Погрешность результатов: {abs(np.exp(m/2) - y_m):.7f}")

head1 = ["x_k", "f'(x_k)_left(погрешность)", "f'(x_k)_center(погрешность)", "f'(x_k)_right(погрешность)", "f''(x_k)(погрешность)", "f'(x_k)_exact", "f''(x_k)_exact"]
data_result = [[], [], [], [], [], []]
for i in range(n):

    if dy_left_k[i] is not None:
        dy_left_error = f"{abs(dy_exact_k[i] - dy_left_k[i]):.4f}"
    else:
        dy_left_error = "None"

    if dy_right_k[i] is not None:
        dy_right_error = f"{abs(dy_exact_k[i] - dy_right_k[i]):.4f}"
    else:
        dy_right_error = "None"

    if dy2_k[i] is not None:
        dy2_error = f"{abs(dy2_exact_k[i] - dy2_k[i]):.4f}"
    else:
        dy2_error = "None"

    if dy_left_k[i] is not None and dy_right_k[i] is not None:
        dy_center_error = f"{abs(dy_exact_k[i] - ((dy_left_k[i] - dy_right_k[i]) / 2)):.4f}"
    else:
        dy_center_error = "None"

    data_result[i].extend([f"{x_k[i]:.4f}", dy_right_error, dy_center_error, dy_left_error, dy2_error, f"{dy_exact_k[i]:.4f}", f"{dy2_exact_k[i]:.4f}"])

dy_left_m, dy_right_m, dy2_m = derivatives(x_k, y_k, m)


if dy_left_m is not None:
    dy_left_m_error = f"{abs(dy_exact_m - dy_left_m):.4f}"
else:
    dy_left_m_error = "None"

if dy_right_m is not None:
    dy_right_m_error = f"{abs(dy_exact_m - dy_right_m):.4f}"
else:
    dy_right_m_error = "None"

if dy2_m is not None:
    dy2_m_error = f"{abs(dy2_exact_m - dy2_m):.4f}"
else:
    dy2_m_error = "None"

if dy_left_m is not None and dy_right_m is not None:
    dy_center_m_error = f"{abs(dy_exact_m - ((dy_left_m - dy_right_m) / 2)):.4f}"
else:
    dy_center_m_error = "None"

data_result[len(data_result) - 1].extend([f"{m:.4f}", dy_right_m_error, dy_center_m_error, dy_left_m_error, dy2_m_error, f"{dy_exact_m:.4f}", f"{dy2_exact_m:.4f}"])

print(tabulate(data_result, headers=head1, tablefmt="grid"))
