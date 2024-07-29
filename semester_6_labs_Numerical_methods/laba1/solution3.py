'''
Метод секущих
'''
import numpy as np
def function(x):
    return 2 * np.exp(-x) - x / 2
def secant_method(x_0, x_previous, epsilon):
    k = 0
    print("итерация k\tx[k] решение")
    print(f"итерация {k}: x[{k+1}] = {x_0:.7f}")
    k += 1
    print(f"итерация {k}: x[{k+1}] = {x_previous:.7f}")
    # x_next - x_(k+1)
    # x_previous - x_(k)
    # x_0 - x_(k-1)
    while True:
        x_next = x_previous - (function(x_previous) / (function(x_previous) - function(x_0))) * (x_previous - x_0)
        k += 1
        print(f"итерация {k}: x[{k+1}] = {x_next:.7f}")
        if abs(x_next - x_previous) < epsilon:
            return x_next
        x_0, x_previous = x_previous, x_next

eps = 1e-7
answer = secant_method(1, 2, eps)
print(f"Результат: {answer:.7f}")



