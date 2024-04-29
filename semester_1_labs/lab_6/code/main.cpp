#include <iostream>
#include "6function.hpp"
using namespace std;

void Read(int n, int a[][SIZE]);
void Write(int n, int a[][SIZE]);
int Summa(int a);
int Max(int n, int a[][SIZE]);
int Min(int n, int a[][SIZE]);

int main()
{
    int n;
    cin >> n;
    auto a = new int[SIZE][SIZE];//автоматическое определение типа данных компилятором для упрощения написания функций ввода и вывода
    Read(n, a);

    int max_el = Max(n, a);
    int min_el = Min(n, a);

    //главное условие задачи
    if (Summa(max_el) == Summa(min_el)) {
        for (int i = 0; i < n; ++i) {
            int selected_index = i;
            int minSumm = INT_MAX;
            for (int k = i; k < n; ++k) {
                int summ = 0;
                for (int j = 0; j < n; ++j) {
                    summ += a[k][j];
                }
                if (minSumm > summ) {
                    selected_index = k;
                    minSumm = summ;
                }
            }

            if (i != selected_index) {
                for (int j = 0; j < n; ++j) {
                    auto t = a[i][j];
                    a[i][j] = a[selected_index][j];
                    a[selected_index][j] = t;
                }
            }
        }
    }
    else {
        cout << "mistake!!!" << endl;
    }

    cout << "////////" << endl;

    Write(n, a);
    cout << "max element: " << max_el << endl;
    cout << "min element: " << min_el << endl;
    cout << "you found the sum of the digits for max element: " << Summa(max_el) << endl;
    cout << "you found the sum of the digits for min element: " << Summa(min_el) << endl;

    return 0;
}




