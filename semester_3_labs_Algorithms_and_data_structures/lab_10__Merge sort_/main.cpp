#include<iostream>
using namespace std;

const int N = 5;
void Main_Merge(int mas[], int const left, int const middle, int const right)
{
    auto const left_size = middle - left + 1;
    auto const right_size = right - middle;

    // Создаем временные массивы
    auto left_mas = new int[left_size];
	auto right_mas = new int[right_size];

    // Копируем данные в временные массивы left[] и right[]
    for (auto i = 0; i < left_size; i++)
        left_mas[i] = mas[left + i];
    for (auto j = 0; j < right_size; j++)
        right_mas[j] = mas[middle + 1 + j];
        

    auto left_index = 0, right_index = 0;
    int index_main = left;

    // Объедините временные массивы обратно в массив[left..right].
    while (left_index < left_size && right_index < right_size) {
        if (left_mas[left_index] <= right_mas[right_index]) {
            mas[index_main] = left_mas[left_index];
            left_index++;
        }
        else {
            mas[index_main] = right_mas[right_index];
            right_index++;
        }
        index_main++;
    }
    // Скопируйте оставшиеся элементы из
    // left[], если таковые имеются
    while (left_index < left_size) {
        mas[index_main] = left_mas[left_index];
        left_index++;
        index_main++;
    }
    // Скопируйте оставшиеся элементы из
    // right[], если таковые имеются
    while (right_index < right_size) {
        mas[index_main] = right_mas[right_index];
        right_index++;
        index_main++;
    }
    
    
        
    //Обязательно освобождаем память от использованных массивов
    delete[] left_mas;
    delete[] right_mas;
}

// begin - для левого индекса, а end - правый индекс подмассива

void MergeSort(int mas[], int const begin, int const end)
{
	
    if (begin >= end)
        return; // Возвращается рекурсивно
    
    auto middle = begin + (end - begin) / 2;
    
    MergeSort(mas, begin, middle);
    MergeSort(mas, middle + 1, end);
    Main_Merge(mas, begin, middle, end);
}


int main()
{
    auto mass = new int[N];

    for (int k = 0; k < N; k++) {
        mass[k] = rand() % 100;
        //cin >> mass[k];
    }
    cout << "Ваш массив: ";
    for (int k = 0; k < N; k++) {
        cout << mass[k] << " ";
    }

    MergeSort(mass, 0, N - 1);
    cout << " " << endl;
    cout << "Отсортированный массив: ";
    for (int k = 0; k < N; k++) {
        cout << mass[k] << " ";
    }
    return 0;
}

