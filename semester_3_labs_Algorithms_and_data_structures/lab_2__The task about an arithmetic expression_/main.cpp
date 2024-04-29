#include <iostream>
#include <cmath>
using namespace std;

float input_number()
{
    float expression = 0;
    for (;;)
    {
        char symbol = cin.get(); //это вызов функции, которая считывает данные из входного потока данных 
        //и ожидает нажатия клавиши ENTER, то есть раздрабливает на кусочки
        if (symbol >= '0' && symbol <= '9')
            expression = expression * 10 + symbol - '0';
        else
        {
            cin.putback(symbol); //возвращаем символ в поток ввода, потому что не подходит
            return expression;
        }
    }
}

//посчитать введенное выражение
float calc();

//функция раскрытия скобок
float parentheses()
{
    char symbol = cin.get();
    if (symbol == '(')
    {
        float x = calc();
        cin.get();
        return x;
    }
    else
    {
        cin.putback(symbol);
        return input_number();
    }
}

//функция умножения и деления
float multip_division()
{
    float x = parentheses();
    for (;;)
    {
        char symbol = cin.get();
        switch (symbol)
        {
        case '*':
            x *= parentheses();
            break;
        case '/':
            x /= parentheses();
            break;
        default:
            cin.putback(symbol);
            return x;
        }
    }
}

//главная функция рассчёта введенного выражения
float calc()
{
    float x = multip_division();
    for (;;)
    {
        char symbol = cin.get();
        switch (symbol)
        {
        case '+':
            x += multip_division();
            break;
        case '-':
            x -= multip_division();
            break;
        default:
            cin.putback(symbol);
            return x;
        }
    }
}


void check_user(float answer) {
    if (answer == INFINITY) {
        cout << "На ноль делить нельзя!";
    }
    else {
        cout << "Результат: " << answer << endl;
    }
}

void print() {
  cout << "Введите выражение: ";
}

int main()
{   
    print();
    float answer = calc();
    check_user(answer);
}
