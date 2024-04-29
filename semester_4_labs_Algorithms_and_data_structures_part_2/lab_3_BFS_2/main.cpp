#include <iostream>
#include <cmath>
#include <set>
#include <vector>
#include <cstdlib>
#include <fstream>
#include <queue>

using namespace std;

int N;

vector <int> roots;
vector <vector<int>> graf;
ofstream out("output.txt");


void BFS(int j, int connect) {  
	queue <int> array_roots;
	array_roots.push(j);

	while (!array_roots.empty()) {
		int k = array_roots.front();
		array_roots.pop();
		for (int i = 0; i < N; i++) {
			if (graf[k][i] == 1 && roots[i] == -1)
			{
				array_roots.push(i);
				roots[i] = connect;
				out << i << " ";
			}
		}
	}

	return;
}

int main()
{
	setlocale(LC_ALL, "Russian");
	ifstream file("input.txt");
    if (!file) {
		cout << "input.txt не существует!" << endl;
	}
	else {
		cout << "input.txt существует" << endl;
	}

	int element;
	file >> N;
	cout << "В данном графе " << N << " вершин" << endl;
	roots = vector<int>(N, -1);

	for (int i = 0; i < N; i++) {
		vector <int> vect;
		for (int j = 0; j < N; j++) {
			file >> element;
			vect.push_back(element);
		}
		graf.push_back(vect);
	}

	int k = 1;
	for (int i = 0; i < N; i++) {
		if (roots[i] == -1) {
			roots[i] = k;
			out << endl << "Компонента связности " << k << ": " << i << " ";
			BFS(i, k);
			k++;
		}
	}
	
	cout << "Смотрите результат в output.txt " << endl;

	return EXIT_SUCCESS;
}
