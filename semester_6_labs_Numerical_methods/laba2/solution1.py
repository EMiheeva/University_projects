'''
Метод Зейделя
'''
import numpy as np
import matplotlib.pyplot as plt

A = np.array([[6.1, -2.2, -1.2, -3.3],
              [7.2, 0.9, 1.8, -4.1],
              [2.8, 3.3, 1.1, 2.5],
              [-1.5, 1.0, 6.3, 0.8]])
b = np.array([-0.50, -2.15, 14.30, -14.00])
x_true_solution = np.array([1.5, 2.0, -2.5, 2.5])

print(x_true_solution)
print("Точное решение: ", np.linalg.solve(A, b))

def seidel_method(A, b, x0, tolerance):
    count = 0
    A_transposition = np.array(A).T.dot(A)
    b_transposition = np.array(A).T.dot(b)
    n = len(x0)
    x_solution = np.copy(x0)

    while True:
        count += 1
        x_0 = np.zeros_like(x_solution)
        for i in range(n):
            sum_1 = A_transposition[i, :i] @ x_0[:i]
            sum_2 = A_transposition[i, i+1:] @ x_solution[i+1:]
            x_0[i] = (b_transposition[i] - sum_1 - sum_2) / A_transposition[i, i]
        if np.allclose(x_solution, x_0, rtol=tolerance):
            break
        x_solution = np.copy(x_0)

    inaccuracy = abs(A @ x_solution - b)

    array_label = ['x1', 'x2', 'x3', 'x4']
    array_x_solution = []
    array_inaccuracy = []
    for i in range(n):
        array_x_solution.append(x_solution[i])
        array_inaccuracy.append(inaccuracy[i])

    print(f"Значение переменной \t\t\tПогрешность")
    for i in range(n):
        print("{:<5}{:<25.15f}{:<25.15f}".format(f"x[{i+1}] = ", array_x_solution[i], array_inaccuracy[i]))
    print("Количество итераций = ", count)

    fig, ax = plt.subplots()
    ax.axis('off')
    ax.table(cellText=np.column_stack((array_label, array_x_solution, np.round(array_inaccuracy, 15))),
             colLabels=["Переменная", "Значение", "Погрешность"], loc='center')
    plt.show()

x0 = np.zeros_like(b)
tolerance = 1e-15
seidel_method(A, b, x0, tolerance)
