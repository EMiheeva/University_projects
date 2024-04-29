#include<iostream>
using namespace std;

const int N = 10;

void shellSort(int mas[], int n)
{
    for (int gap = n/2; gap > 0; gap /= 2) 
    {   
        for (int i = gap; i < n; i += 1) 
        {   
            int temp = mas[i];
            int j;           
            for (j = i; (j >= gap && temp < mas[j - gap]); j -= gap)
                mas[j] = mas[j - gap];
            mas[j] = temp;
        }
    }
}

int main()
{
	auto mass = new int[N];

	for (int k = 0; k < N; k++) {
		mass[k] = rand() % 27;
	}
	cout << "Рандомный массив: ";
	for (int k = 0; k < N; k++) {
		cout << mass[k] << " ";
	} 
	
	cout << "" <<endl;
	cout << "Ваш массив: ";
	for (int k = 0; k < N; k++) {
		cout << mass[k] << " ";
	}
    cout << "" <<endl;

	ShellSort(mass, N);
	cout << "Отсортированный массив: ";
	for (int k = 0; k < N; k++) {
		cout << mass[k] << " ";
	}
	return 0;
}
