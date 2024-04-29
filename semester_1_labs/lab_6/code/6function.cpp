#include <iostream>
#include "6function.hpp"

void Read(int n, int a[][SIZE]) {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            std::cin >> a[i][j];
        }
    }
}

void Write(int n, int a[][SIZE]) {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            std::cout << a[i][j] << " ";
        }
        std::cout << std::endl;
    }
}

int Summa(int a) {
    int res = 0;
    if (a < 0) {
        a = -a;
    }
    while (a > 0) {
        res += a % 10;
        a /= 10;
    }
    return res;
}

int Max(int n, int a[][SIZE]) {
    int max_e = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (a[i][j] > max_e) {
                max_e = a[i][j];
            }
        }
    }
    return max_e;
}


int Min(int n, int a[][SIZE]) {
    int min_e = 10000;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (a[i][j] < min_e) {
                min_e = a[i][j];
            }
        }
    }
    return min_e;
}
