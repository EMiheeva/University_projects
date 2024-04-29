//Алгоритм Джарвиса
#include <iostream>
using namespace std;

const int N = 100;

struct Point
{
    int x;
    int y;
};

// Для нахождения местоположения точки С относительно прямой АВ
// 0 - на одной прямой
// 1 - по часовой стрелке
// 2 - против часовой стрелки
int orientation(Point A, Point B, Point C)
{
    int formula = (C.x - B.x) * (B.y - A.y) - (C.y - B.y) * (B.x - A.x);

    if (formula == 0)
        return 0;
    return (formula > 0) ? 1 : 2;
}

void Jarvis(Point points[], int n)
{
    if (n < 3) {
        cout << "Выпуклой оболочки не существует." << endl;
        return;
    }

    // Храним результат
    int result[N];
    for (int i = 0; i < N; i++)
        result[i] = -1;

    // Ищем самую левую точку
    int left = 0;
    for (int i = 1; i < n; i++)
        if (points[i].x < points[left].x)
            left = i;

    // Начинаем с крайней левой точки, продолжаем двигаться против часовой стрелки
    // пока снова не достигнем начальной точки
    int p = left, q;
    do {
        // Ищем точку 'q' такую, что тройка (p, i, q)
        // против часовой стрелки для всех точек 'i'
        q = (p + 1) % n;
        for (int i = 0; i < n; i++)
            if (orientation(points[p], points[i], points[q]) == 2)
                q = i;

        result[p] = q; 
        p = q; 
    } while (p != left);

    //Проверить на существование одинаковых точек
    for (int i = 0; i < n; i++) {
        if ((points[i].x == points[i - 1].x) && (points[i].y == points[i - 1].y)) {
            result[i] = -1;
        }
    }

    int counter = 0;
    for (int i = 0; i < n; i++) {
        if (result[i] != -1) {
            counter += 1;
        }
    }
    if (counter < 3) {
        cout << "Все точки одинаковые. Выпуклой оболочки нет." << endl;
        return;
    }
    else {
        cout << "Выпуклая оболочка существует и состоит из точек: " << endl;
        for (int i = 0; i < n; i++) {
            if (result[i] != -1) {
                cout << "(" << points[i].x << ", " << points[i].y << ")\n";
            }
        }

    }
}

int main()
{
    setlocale(LC_ALL, "Rus");
    int n;
    cout << "Введите кол-во точек: ";
    cin >> n;
    Point points[N];
    cout << "Введите координаты " << n << " точек: " << endl;
    for (int i = 0; i < n; i++) {
        cout << i + 1 << " точка: ";
        cin >> points[i].x >> points[i].y;
    }
    Jarvis(points, n);
    return 0;
}
