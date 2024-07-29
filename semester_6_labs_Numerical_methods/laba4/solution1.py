'''
Интерполяционная схема Эйткена
'''
import numpy as np

def aitken_interpolation(x, a, b):
    if b - a != 1:
        aitken_matrix[a][b] = (1 / (x_k[b] - x_k[a])) * (aitken_interpolation(x, a, b - 1) * (x_k[b] - x) - aitken_interpolation(x, a + 1, b) * (x_k[a] - x))
        #print(f"aitken_matrix[{a}][{b}] = {aitken_matrix[a][b]:.6f}")
        return aitken_matrix[a][b]
    else:
        aitken_matrix[a][b] = (1 / (x_k[b] - x_k[a])) * (y_k[a] * (x_k[b] - x) - y_k[b] * (x_k[a] - x))
        #print(f"aitken_matrix[{a}][{b}] = {aitken_matrix[a][b]:.6f}")
        return aitken_matrix[a][b]

x_k = [1.00, 1.08, 1.20, 1.27, 1.31, 1.38]
y_k = [1.17520, 1.30254, 1.50946, 1.21730, 1.22361, 1.23470]
x_star = 1.030
n = len(x_k)
aitken_matrix = np.zeros((n, n))
result = aitken_interpolation(x_star, 0, n - 1)

print("Матрица Интерполяционной схемы Эйткена:")
for row in aitken_matrix:
    for value in row:
        print(f"{value:.6f}", end=" ")
    print()
print(f"\nЗначение функции f(x*), где x* = {x_star}")
print(f"По интерполяционной схеме Эйткена: {aitken_matrix[0][5]}")
print(f"Результат с точностью h = 0.000001: {aitken_matrix[0][5]:.6f} ")
