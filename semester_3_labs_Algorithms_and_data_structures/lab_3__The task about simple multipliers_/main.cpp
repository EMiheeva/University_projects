#include <iostream>
#include <cstdlib>
#include <cmath>

using namespace std;

int main() {
  setlocale(LC_ALL, "Rus");
  int x;
  cout << "Введите число: " << endl;
  cin >> x;
  for (int k = 1; k <= x; k *= 3) {
    for (int l = 1; k*l <= x; l*= 5) {
      for (int m = 1; k*l*m <= x; m*=7) {
        cout << k*l*m << endl;
      }
    }
  }
  
  if (x <= 0) {
    cout << "Ошибка: Введено число, меньшее 0";
  }
  
  return 0;
}
