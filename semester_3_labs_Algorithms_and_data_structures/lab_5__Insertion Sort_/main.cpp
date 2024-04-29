#include<iostream>
using namespace std;

const int N = 10;


void InsertionSort(int mas[], int n)
{
    int i, j, key;
    for (i = 1; i < n; i++)
    {
        key = mas[i];
        j = i - 1;
 
        while (j >= 0 && mas[j] > key)
        {
            mas[j + 1] = mas[j];
            j = j - 1;
        }
        mas[j + 1] = key;
    }
}


int main()
{
	auto mass = new int[N];
	
    cout << "Введите 10 элементов типа int вашего массива: " <<endl;
    
    for (int k = 0; k < N; k++) {
		cin >> mass[k];
	}
	cout << "Ваш массив: ";
	for (int k = 0; k < N; k++) {
		cout << mass[k] << " ";
	}
    cout << "" <<endl;

	InsertionSort(mass, N);
	cout << "Отсортированный массив: ";
	for (int k = 0; k < N; k++) {
		cout << mass[k] << " ";
	}
	return 0;
}
