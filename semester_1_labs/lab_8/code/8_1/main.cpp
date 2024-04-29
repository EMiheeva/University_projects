
#include <iostream>

//Функция для нахождения чисел с одинаковыми цифрами
bool the_same_digit(int a) {

    int digit_1 = 0;
    int digit_2 = 0;
    digit_1 = a % 10;
    while (a >= 10) {
        a /= 10;
        digit_2 = a % 10;
        if (digit_2 != digit_1) {
            return false;
        }
        digit_1 = digit_2;
    }
    return true;
}


int main()
{   
    int n;
    const int size = 1000;
    int count = 0;
    int* mas = new int[size];
    std::cin >> n; //вводим кол-во элементов
    for (int i = 0; i < n; ++i) {
        std::cin >> mas[i];
    }

    for (int i = 0; i < n; ++i) {
        if (the_same_digit(mas[i])) {
            count += 1;
            //std::cout<<the_same_digit(mas[i])<<std::endl;
        }
        //std::cout<<count<<std::endl;
    }

    if (count >= 3) {
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (mas[i] < mas[j]) {
                    std::swap(mas[i], mas[j]);
                }
            }
        }
    }
    else {
        std::cout << "Нет трех чисел с одинаковыми цифрами" << std::endl;
    }


    for (int i = 0; i < n; ++i) {
        std::cout << mas[i] << " ";
    }

    delete[] mas;

    return 0;
}
