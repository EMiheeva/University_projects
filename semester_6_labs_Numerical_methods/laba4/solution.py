'''
Интерполяционный многочлен Лагранжа
'''
import numpy as np
import sympy as sp

x_k = np.array([8.0, 8.5, 9.0, 9.5])
y_k = np.array([2.079, 2.140, 2.197, 2.251])
x = 8.2

def lagrange(x_k, y_k):
    x = sp.symbols('x')
    n = len(x_k)
    result_lagrange = 0
    for i in range(n):
        lagrange_i = 1
        for j in range(n):
            if i != j:
                lagrange_i *= (x - x_k[j]) / (x_k[i] - x_k[j])
        result_lagrange += y_k[i] * lagrange_i
    return result_lagrange
    

polinom_lagrange = lagrange(x_k, y_k)
print(f"1) Интерполяционный многочлен Лагранжа L(x) = \n{polinom_lagrange}")

y_exact = np.log(x)
y_lagrange = polinom_lagrange.subs(sp.symbols('x'), x)
print(f"2) Аналитическое значение f(x) = f({x}) = {round(y_exact, 6)}")
print(f"3) Значение многочлена Лагранжа в точке L(x) = L({x}) = {round(y_lagrange, 6)}")


step_h = 1e-7
f = sp.lambdify(sp.symbols('x'), polinom_lagrange)

df_exact = 1/x
df_left = (f(x) - f(x - step_h)) / step_h
df_right = (f(x + step_h) - f(x)) / step_h
df_center = (f(x + step_h) - f(x - step_h)) / (2 * step_h)

print()
print(f"4) Левая производная в точке x = {x}: {round(df_left, 10)}")
print(f"5) Центральная производная в точке x = {x}: {round(df_center, 10)}")
print(f"6) Правая производная в точке x = {x}: {round(df_right, 10)}")
print(f"7) Точное значение производной в точке x = {x}: {round(df_exact, 10)}")
print()
print("= Подсчет погрешностей =")
print(f"8) Погрешность метода Лагранжа в точке x = {x}: {round(abs(y_lagrange - y_exact), 10)}")
print(f"9) Погрешность левой производной: {round(abs(df_left - df_exact), 10)}")
print(f"10) Погрешность правой производной: {round(abs(df_right - df_exact), 10)}")
print(f"11) Погрешность центральной производной: {round(abs(df_center - df_exact), 10)}")
