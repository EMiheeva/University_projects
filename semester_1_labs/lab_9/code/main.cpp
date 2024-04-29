//без использования ООП
#include <SFML/Graphics.hpp>
#include <vector>
#include <thread>
#include <chrono>

using namespace std::chrono_literals;
int main()
{
    sf::RenderWindow window(sf::VideoMode(1200, 500), "SFML works!");

    //Первый синий прямоугольник
    sf::RectangleShape rectangle(sf::Vector2f(200.f, 100.f));//создание
    rectangle.setFillColor(sf::Color::Blue);//цвет
    int rectangle_x = 970, rectangle_y = 0;//начальные координаты
    rectangle.setPosition(rectangle_x, rectangle_y);//начальная позиция


    //Второй желтый прямоугольник
    sf::RectangleShape rectangle2(sf::Vector2f(150.f, 90.f));//создание
    rectangle2.setFillColor(sf::Color::Yellow);//цвет
    int rectangle2_x2 = 980, rectangle2_y2 = 0;//начальные координаты
    rectangle2.setPosition(rectangle2_x2, rectangle2_y2);//начальная позиция


    //Третий красный прямоугольник
    sf::RectangleShape rectangle3(sf::Vector2f(120.f, 70.f));//создание
    rectangle3.setFillColor(sf::Color::Red);//цвет
    int rectangle3_x3 = 990, rectangle3_y3 = 0;//начальные координаты
    rectangle3.setPosition(rectangle3_x3, rectangle3_y3);//начальная позиция


    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();
        }
 
        rectangle_x -= 2;
        rectangle_y += 2;
        if (rectangle_y > 450) {
            rectangle_y = 450;
            rectangle_x--;
            if (rectangle_x < 20) {
                rectangle_x = 20;
            }
        }
        rectangle.setPosition(rectangle_x, rectangle_y);


        rectangle2_x2 -= 3;
        rectangle2_y2 += 3;
        if (rectangle2_y2 > 450) {
            rectangle2_y2 = 450;
            rectangle2_x2--;
            if (rectangle2_x2 < 20) {
                rectangle2_x2 = 20;
            }
        }
        rectangle2.setPosition(rectangle2_x2, rectangle2_y2);


        rectangle3_x3 -= 1;
        rectangle3_y3 += 1;
        if (rectangle3_y3 > 450) {
            rectangle3_y3 = 450;
            rectangle3_x3--;
            if (rectangle3_x3 < 20) {
                rectangle3_x3 = 20; //т.к. не получается 
            }
        }
        rectangle3.setPosition(rectangle3_x3, rectangle3_y3);


        window.clear();
        window.draw(rectangle);
        window.draw(rectangle2);
        window.draw(rectangle3);
        window.display();

        std::this_thread::sleep_for(7ms);
    }

    return 0;
}
