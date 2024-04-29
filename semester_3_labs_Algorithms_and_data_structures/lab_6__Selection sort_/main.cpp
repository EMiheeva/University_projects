#include<iostream>
using namespace std;

const int N = 10;

 
void selectionSort(int mas[], int n)
{
    int i, j, min_index;
 
    // Один за другим перемещают границу
    // несортированный массив
    for (i = 0; i < n-1; i++)
    {
       
        // Найти минимальный элемент в
        // несортированном массиве
        min_index = i;
        for (j = i+1; j < n; j++)
        if (mas[j] < mas[min_index])
            min_index = j;
 
        // Поменяйте найденный минимальный элемент
        // с первым элементом
        if(min_index!=i)
            swap(mas[min_index], mas[i]);
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

	selectionSort(mass, N);
  
	cout << "Отсортированный массив: ";
	for (int k = 0; k < N; k++) {
		cout << mass[k] << " ";
	}
	return 0;
}
