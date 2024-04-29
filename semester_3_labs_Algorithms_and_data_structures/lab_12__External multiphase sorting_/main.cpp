//самая трудная лабораторная работа

#include <iostream>
#include <fstream>
using namespace std;
int main()
{
	ifstream in, A_in, B_in;
	ofstream out, A_out, B_out;

	int count_elem_from_in = 0,
		gap,
		A_output, B_output,
		A_size, B_size;

	bool check = true,
		A_is_full, B_is_full;

	out.open("result.txt");

	if (!in) {
		cout << "Add input.txt!" << endl;
	}
	else {
		cout << "input.txt is exist!" << endl;
		in.open("input.txt");
	}

	while (in >> A_output) {
		out << A_output << " ";
		count_elem_from_in++;
	}

	in.close();
	out.close();

	/*В многофазной сортировке важно распределение элементов с помощью серий. Длина серий фиксируется на каждом шаге.
	В исходном файле все серии имеют длину 1,
	после первого шага она равна 2, 
	после второго шага – 4,
	после k-го шага – 2k*/
	
	//start
	for (int series = 1; series < count_elem_from_in; series *= 2) {
		//Исходный файл разбивается на два вспомогательных файла 
		in.open("result.txt");
		A_out.open("A.txt");
		B_out.open("B.txt");
		gap = 0;

		while (in >> A_output) {
			cout << "series iteration: " << series << endl;
			gap++;
			cout << "gap in loop: " << gap << endl;
			if (check) {
				A_out << A_output << " ";
				cout << "check A: " << check << " gap: " << gap << endl;
			}
			else {
				B_out << A_output << " ";
				cout << "check B: " << check << " gap: " << gap << endl;
			}
			
			if (gap == series) {
				gap = 0;
				check = !check;
			}
			cout << "gap after two's if: " << gap << endl;
			cout << "/////////////////////////////////////////////" << endl;
		}
		
		in.close();
		A_out.close();
		B_out.close();


		A_in.open("A.txt");
		B_in.open("B.txt");
		out.open("result.txt");
		//вспомогательные файлы сливаются в файл 
		// при этом одиночные элементы образуют упорядоченные пары.
		if (A_in >> A_output)
			A_is_full = true;
		else
			A_is_full = false;

		if (B_in >> B_output)
			B_is_full = true;
		else
			B_is_full = false;
		//Полученный файл обрабатывается
		//При этом упорядоченные пары переходят в упорядоченные четверки.

		for (int i = 0; i < count_elem_from_in; i += 2 * series)
		{
			A_size = 0; 
			B_size = 0;
			while (A_size < series && A_is_full && B_size < series && B_is_full) {
				//Сравниваем элементы
				if (A_output < B_output) {
					out << A_output << " ";
					if (A_in >> A_output)
						A_is_full = true;
					else
						A_is_full = false;
					A_size++;
				}
				else {
					out << B_output << " ";
					if (B_in >> B_output)
						B_is_full = true;
					else
						B_is_full = false;
					B_size++;
				}
			}
			//Повторяя шаги, сливаем четверки в восьмерки и т.д.,
			//каждый раз удваивая длину слитых последовательностей до тех пор, пока не будет упорядочен целиком весь файл
			//Слияние А и В
			while (A_size < series && A_is_full) {
				out << A_output << " ";
				if (A_in >> A_output)
					A_is_full = true;
				else
					A_is_full = false;
				A_size++;
			}

			while (B_size < series && B_is_full) {
				out << B_output << " ";
				if (B_in >> B_output)
					B_is_full = true;
				else
					B_is_full = false;
				B_size++;
			}

		}
		A_in.close();
		B_in.close();
		out.close();
		
	}
	//end
	cout << "Look result.txt" << endl;
	return 0;
}
