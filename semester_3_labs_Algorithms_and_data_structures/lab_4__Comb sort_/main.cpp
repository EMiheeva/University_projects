#include<iostream>
using namespace std;

const int N = 10;

// Для нахождения промежутка между элементами
int GetNextGap(int gap)
{
	// Уменьшение промежутка на коэффициент 
	gap = (gap*N)/1.3;
	if (gap < 1)
		return 1;
	return gap;
}

void CombSort(int mas[], int n)
{
	// Инициализация промежутка
	int gap = n;

	// Инициализируем чек-поинт как true, чтобы убедиться, что цикл выполняется
	bool check_point = true;

	// Выполняем цикл, пока промежуток больше 1 и последняя
	// итерация совершила обмен элементами
	while (gap != 1 || check_point == true)
	{
		// Следующий промежуток
		gap = GetNextGap(gap);

		// Инициализируем чек-поинт как false, чтобы мы могли
		// проверить, произошел ли обмен элементами
		check_point = false;

		// Сравнить все элементы с текущим промежутком, хранящимся в gap
		for (int i=0; i<n-gap; i++)
		{
			if (mas[i] > mas[i+gap])
			{
				swap(mas[i], mas[i+gap]);
				check_point = true;
			}
		}
	}
}

int main()
{
auto mass = new int[N];
	
  cout << "Введите 10 элементов типа int вашего массив: " <<endl;
    
  for (int k = 0; k < N; k++) {
		cin >> mass[k];
	}
  
	cout << "Ваш массив: ";
	for (int k = 0; k < N; k++) {
		cout << mass[k] << " ";
	}
  cout << "" <<endl;
  
	CombSort(mass, N);
	
  cout << "Отсортированный массив: ";
	for (int k = 0; k < N; k++) {
		cout << mass[k] << " ";
	}
	return 0;
}
