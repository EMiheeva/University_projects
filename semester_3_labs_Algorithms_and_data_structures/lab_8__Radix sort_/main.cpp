#include<iostream>
using namespace std;

const int N = 8;

//узнать сколько разрядов в большом числе
int getMax(int mas[], int n)
{
    int max_mas = mas[0];
    for (int i = 1; i < n; i++)
        if (mas[i] > max_mas)
            max_mas = mas[i];
    return max_mas;
}
 
void BucketSort(int mas[], int n, int discharge)
{
    int bucket[n]; 
    auto count_digits = new int[10];
    int i = 0;
    
	//LSD (least significant digit)
	//Сначала по единицам, десяткам и сотням
    for (i = 0; i < n; i++) {
        count_digits[(mas[i] / discharge) % 10]++;
    }
        
	//положение единиц, десяток и сотен
    for (i = 1; i < 10; i++) {
        count_digits[i] += count_digits[i - 1];
    }
    
    //создать отсортированный массив
    for (i = n - 1; i >= 0; i--) {
        bucket[count_digits[(mas[i] / discharge) % 10] - 1] = mas[i];
        count_digits[(mas[i] / discharge) % 10]--;
    }
    for (i = 0; i < n; i++)
        mas[i] = bucket[i];
        
    cout << "Результат: " << endl;
    for (i = 0; i < n; i++)
        cout << bucket[i] << " ";
    cout << " " << endl;
}
 
void Radixsort(int mas[], int n)
{
    int max_elem = getMax(mas, n);
    //сколько раз сортировать
    for (int discharge = 1; max_elem / discharge > 0; discharge *= 10)
        BucketSort(mas, n, discharge);

}
 


int main()
{
	auto mass = new int[N];

	for (int k = 0; k < N; k++) {
		mass[k] = rand() % 27;
	}
	cout << ""<< endl;

	Radixsort(mass, N);
	cout << "Отсортированный массив: ";
	for (int k = 0; k < N; k++) {
		cout << mass[k] << " ";
	}
	return 0;
	
}
