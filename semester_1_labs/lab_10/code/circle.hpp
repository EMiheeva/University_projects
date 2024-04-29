#pragma once
#include <SFML/Graphics.hpp>
#include <iostream>
namespace std
{
	class Circle //класс создан в динамической памяти
	{
	public:
		Circle(int x, int y, float r, float v);
		~Circle();
		//Get - получить
		//Функция, к-я будет получать фигуру
		sf::CircleShape* Get();  //используем указатель, чтобы не создавать копии, к-ые занимают память
		void Move();
		//Set - установить, определить
		void SetY(int y);
		int GetY();
	private:
		int m_x, m_y; //координаты центра окр-ти
		float m_r; //радиус окружности
		float m_v; //скорость
		sf::CircleShape* m_ball;
	};
}
