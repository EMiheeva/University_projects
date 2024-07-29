'''
Метод Гаусса
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

def gauss_metod(A, b):
    count = 0
    n = len(A)
    A_and_b = np.concatenate((A, b.reshape(n, 1)), axis=1)
    # А вот и прямой ход.
    for i in range(n):
        count += 1
        # Выбор главного элемента
        max_element_in_row = i + np.argmax(np.abs(A_and_b[i:, i]))
        A_and_b[[i, max_element_in_row]] = A_and_b[[max_element_in_row, i]]
        for j in range(i + 1, n):
            A_and_b[j] -= A_and_b[i] * A_and_b[j, i] / A_and_b[i, i]
    print(f'Количество итераций = {count}')

    # Обратный ход. Инициируем столбец решения.
    x_solution = np.zeros(n)
    for i in range(n-1, -1, -1):
        x_solution[i] = (A_and_b[i, n] - A_and_b[i, i+1:n].dot(x_solution[i + 1:n])) / A_and_b[i, i]

    # Для погрешности
    inaccuracy = np.zeros(n)
    for i in range(n):
        inaccuracy[i] = np.abs(np.sum(A[i] * x_solution) - b[i])

    array_label = ['x1', 'x2', 'x3', 'x4']
    array_x_solution = []
    array_inaccuracy = []
    for i in range(n):
        array_x_solution.append(x_solution[i])
        array_inaccuracy.append(inaccuracy[i])

    print(f"Значение переменной \t\t\tПогрешность")
    for i in range(n):
        print("{:<5}{:<25.15f}{:<25.15f}".format(f"x[{i+1}] = ", array_x_solution[i], array_inaccuracy[i]))

    fig, ax = plt.subplots()
    ax.axis('off')
    ax.table(cellText=np.column_stack((array_label, array_x_solution, np.round(array_inaccuracy, 15))),
             colLabels=["Переменная", "Значение", "Погрешность"], loc='center')
    plt.show()

gauss_metod(A, b)

