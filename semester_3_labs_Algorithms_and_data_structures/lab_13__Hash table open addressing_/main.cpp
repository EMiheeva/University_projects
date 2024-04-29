//Благодаря этом ресурсу, тема хеш-таблица стали немного понятна
..https://www.geeksforgeeks.org/implementing-hash-table-open-addressing-linear-probing-cpp/
#include <iostream>
using namespace std;

template <typename K, typename V>

class HashNode {
public:
	V value;
	K key;

	// Конструтор
	HashNode(K key, V value)
	{
		this->value = value;
		this->key = key;
	}
};

template <typename K, typename V>

// Хеш-таблица
class HashMap {

	HashNode<K, V>** table;
	int main_size;
	int size;

	HashNode<K, V>* fictiv_node;

public:
	HashMap()
	{
		
		main_size = 20; //например
		size = 0;
		table = new HashNode<K, V>*[main_size];

		// Инициализировать все элементы массива как NULL
		for (int i = 0; i < main_size; i++)
			table[i] = NULL;

		// Фиктивный узел равен -1
		fictiv_node = new HashNode<K, V>(-1, -1);
	}


	int hashCode(K key)
	{
		return key % main_size;
	}

	// Функция для добавления пары ключ-значение
	void InsertNode(K key, V value)
	{
		HashNode<K, V>* temp = new HashNode<K, V>(key, value);

		// Применение хэш-функции для поиска индекса по заданному ключу
		int hashIndex = hashCode(key);

		// find next free space
		while (table[hashIndex] != NULL && table[hashIndex]->key != key&& table[hashIndex]->key != -1) {
			hashIndex++;
			hashIndex %= main_size;
		}

		// если новый узел должен быть вставлен, то
		// увеличить текущий размер
		if (table[hashIndex] == NULL || table[hashIndex]->key == -1)
			size++;
		table[hashIndex] = temp;
	}

	// Функция для удаления пары ключ-значение
	V DeleteNode(int key)
	{
		// Применить хэш-функцию
		// чтобы найти индекс для заданного ключа
		int hash_index = hashCode(key);

		// поиск узла с заданным ключом
		while (table[hash_index] != NULL) {
			// если найден
			if (table[hash_index]->key == key) {
				HashNode<K, V>* temp = table[hash_index];

				// Вставить фиктивный узел для дальнейшего использования
				table[hash_index] = fictiv_node;

				// Уменьшить размер
				size--;
				return temp->value;
			}
			hash_index++;
			hash_index %= main_size;
		}

		// если не найдено
		return 0;
	}

	// Функция для поиска значения по заданному ключу
	V FindNode(int key)
	{
		// Применение хэш-функции для поиска индекса заданного ключа
		int hash_index = hashCode(key);
		int count = 0;

		// finding the node with given key
		while (table[hash_index] != NULL) { 
    // int counter =0

			if (count++ > main_size) // избежать бесконечного цикла
				return 0;
        
			if (table[hash_index]->key == key)
				return table[hash_index]->value;
			hash_index++;
			hash_index %= main_size;
		}

		// Если не найдено
		return 0;
	}
  
	int size_table()
	{
		return size;
	}
  
	bool check_empty()
	{
		return size == 0;
	}

	// Функция для отображения сохраненных пар ключ-значение
	void display()
	{
		for (int i = 0; i < main_size; i++) {
			if (table[i] != NULL && table[i]->key != -1)
				cout << "key = " << table[i]->key
				<< " value = "
				<< table[i]->value << endl;
		}
	}
};

int main()
{
	HashMap<int, int>* h = new HashMap<int, int>;
	h->InsertNode(1, 1);
	h->InsertNode(2, 2);
	h->InsertNode(2, 3);
	h->display();
	cout << h->size_table() << endl;
	cout << h->DeleteNode(2) << endl;
	cout << h->size_table() << endl;
	cout << h->check_empty() << endl;
	cout << h->FindNode(2);
	return 0;
}
