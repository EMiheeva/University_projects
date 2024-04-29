#include "circle.hpp"
#include <iostream>
namespace std
{

	Circle::Circle(int x, int y, float r, float v)
	{
		m_x = x;
		m_y = y;
		m_r = r;
		m_v = v;
		m_ball = new sf::CircleShape(r); //динамический объект, значит не забыть удалить в деструкторе!
		m_ball->setOrigin(m_r, m_r); //для обращения к ф-ии используем вместо "." - "->"
		m_ball->setFillColor(sf::Color::Blue); //зададим цвет шарикам
		m_ball->setPosition(m_x, m_y); //задали расположение
	}
	Circle::~Circle()
	{
		delete m_ball;
	}

	//Get - получить
	//Функция, к-я будет получать фигуру
	sf::CircleShape* Circle::Get() { return m_ball; } //используем указатель, чтобы не создавать копии, к-ые занимают память

	void Circle::Move() {
		m_y += m_v;
		m_ball->setPosition(m_x, m_y);//на каждой итерации придаем новые координаты
	}

	//Set - установить, определить
	void Circle::SetY(int y) {
		m_y = y;
		m_ball->setPosition(m_x, m_y);
	}

	int Circle::GetY() { return m_y; }
}
