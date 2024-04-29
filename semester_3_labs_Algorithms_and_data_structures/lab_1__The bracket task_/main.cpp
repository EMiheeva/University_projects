#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

int main() {
    setlocale(LC_ALL, "Rus");
    bool check = true; //стек, хранящий открывающие скобки. Оценивает сверху.
    vector <char> stack;
    string s;
    cout << "Введите строку: " << endl;
    cin >> s;


    for (int i = 0; i < s.length(); i++) {
        if ((s[i] == '(') || (s[i] == '[') || (s[i] == '{')) {
            stack.push_back(s[i]); //добавляем открывающиеся скобки трех видов в конец вектора
        }

        if (s[i] == ')') {
            if (stack.back() == '(') {
                stack.pop_back(); //нашли пару, удалили
            }
            else {
                check = false; //не нашлось открытой скобки
				cout << "Строка не существует";
            }
        }

        if (s[i] == ']') {
            if (stack.back() == '[') {
                stack.pop_back();
            }
            else {
                check = false;
				cout << "Строка не существует";
            }
        }

        if (s[i] == '}') {
            if (stack.back() == '{') {
                stack.pop_back();
            }
            else {
                check = false;
				cout << "Строка не существует";
            }
        }

        if ((s[i] != ')') && (s[i] != ']') && (s[i] != '}') && (s[i] != '(') && (s[i] != '[') && (s[i] != '{')) {
            cout << "Строка содержит лишние символы" << endl;
            check = false;
            break;
        }

    }

    if (check) {
        cout << "Строка существует";

    return 0;
    }
}
