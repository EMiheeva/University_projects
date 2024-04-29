#include <iostream>
#include <chrono>
using namespace std;

const int N = 10;

int mediana (int a, int b, int c)
{
  if (a > b) { 
    if (c > a) 
      return a;
    return (b > c) ? b : c;
  } 
  
  if (c > b) 
    return b;
  return (a > c) ? a : c; 
}


void QuickSort(int mas[], int left, int right) {
	if (left == right) return; 
	
	int pivot = mediana(mas[left], mas[right], mas[(right+left)/2]); //поиск опорного элемента с помощью медианы трёх
                                                                   //гарантированный способ нахождения
	
  //int pivot = mas[(left + right) / 2]; //поиск опорного элемента простым путем
	//cout << "pivot: "<< pivot << endl; //опорный элемент, по которому разделяется массив
	
  int i = left;
	int j = right;
	while (i <= j) {
		while (mas[i] < pivot)
			i++;
		while (mas[j] > pivot)
			j--;
		if (i >= j)
			break;//так как сортируем по возрастанию, а i - это первый левый элемент
		swap(mas[i++], mas[j--]); //основная суть сортировки
	}
	
	
	//Разбиение Хоара
	QuickSort(mas, left, j);
	
	QuickSort(mas, j + 1, right);
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

	QuickSort(mass, 0, N - 1);
	cout << "Отсортированный массив: ";
	for (int k = 0; k < N; k++) {
		cout << mass[k] << " ";
	}
	return 0;
}
