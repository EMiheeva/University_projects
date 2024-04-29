#include<iostream>
using namespace std;

const int N = 10;


void heapify(int mas[], int N, int root)
{
 
    int largest = root;//root = 0
    int left = 2*root + 1;
    int right = 2*root + 2;
    //основное правило его построения, заключается в том 
    //что левый потомок меньше текущего узла, а правый потомок больше.
    if (N > left && mas[left] > mas[largest])
        largest = left;
 
    if (N > right && mas[right] > mas[largest])
        largest = right;
 
    if (largest != root) {
        swap(mas[root], mas[largest]);
        heapify(mas, N, largest);
    }
}
//строится снизу вверх
void heapSort(int mas[], int N)
{
    for (int i = N / 2 - 1; i >= 0; i--)
        heapify(mas, N, i);
 
    for (int i = N - 1; i >= 0; i--) {
        swap(mas[0], mas[i]);  // Главная идея: Перемещаем текущий корень в конец
        heapify(mas, i, 0);  // вызываем процедуру heapify на уменьшенной куче
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

	heapSort(mass, N);
	cout << "Отсортированный массив: ";
	for (int k = 0; k < N; k++) {
		cout << mass[k] << " ";
	}
	return 0;
}
