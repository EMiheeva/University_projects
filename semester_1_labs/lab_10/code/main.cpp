#include <SFML/Graphics.hpp>
#include <iostream>
#include <vector>
#include "circle.hpp"

int main()
{   
    //инициализация времени
    srand(time(0));
    sf::RenderWindow window(sf::VideoMode(800, 800), L"ПРЕДПОСЛЕДНЯЯ_ЛАБА_10_ВАРИАНТ_8");
    //создание фигур с помощью вектора
    const int N = 20; //для примера!
    std::vector<std::Circle*> shapes;
    for (int i = 0; i < 780; i += 780 / N)
        shapes.push_back(new std::Circle(i, 50, 10, rand() % 5 + 1)); 
        // генерирую случайную скорость, "+1" для избежания нулевой скорости

    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();
        }
        for (const auto& shape : shapes) {
            shape->Move();
            if (shape->GetY() > 780) {  //Если "у" выходит за границу экрана, то
                shape->SetY(780); //присвоить эту координату - остановить фигурки
            }
        }

        window.clear();
        //shape - это указатель, чтобы получить значение по указателю, его нужно разименовать
        //отображение фигурок
        for (const auto& shape : shapes)
            window.draw(*shape->Get());

        window.display();
    }
    //очистка памяти после использования дин-й памяти
    for (const auto& shape : shapes)
        delete shape;
    return 0;
}
