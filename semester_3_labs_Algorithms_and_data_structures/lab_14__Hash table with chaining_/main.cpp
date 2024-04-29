#include<iostream>
#include<list>
using namespace std;

class Hash
{
	int BUCKET;
  list<int>* table; // Указатель на массив, содержащий BUCKET

public:
	Hash(int V); // конструктор

	void Insert_element(int x);
	void Delete_element(int key);
	int hashFunction(int x) {
		return (x % BUCKET);
	}
	void displayHash();
  
};

Hash::Hash(int b)
{
	this->BUCKET = b;
	table = new list<int>[BUCKET];
}

void Hash::Insert_element(int key)
{
	int index = hashFunction(key);
	table[index].push_back(key);
}

void Hash::Delete_element(int key)
{
	// получить хеш-индекс ключа
	int index = hashFunction(key);

	// найти ключ в списке индексов
	list <int> ::iterator i;
  // Обход списка с помощью итератора
	for (i = table[index].begin(); i != table[index].end(); i++) {
		if (*i == key)
			break;
	}

	// если ключ найден в хеш-таблице, удалить его
	if (i != table[index].end())
		table[index].erase(i);
}


void Hash::displayHash() {
	for (int i = 0; i < BUCKET; i++) {
		cout << i;
		for (auto x : table[i])
			cout << " --> " << x;
		cout << endl;
	}
}

int main()
{
	// массив, содержащий ключи для сопоставления в хеш-таблицу
	int a[] = { 15, 11, 27, 8, 12 };
	int n = sizeof(a) / sizeof(a[0]); // формула нахождения размера массива
  
	Hash h(7); // 7 - это количество ячеек в
				// хеш-таблице
	for (int i = 0; i < n; i++)
		h.Insert_element(a[i]);
	h.Delete_element(12);
	h.displayHash();

	return 0;
}

