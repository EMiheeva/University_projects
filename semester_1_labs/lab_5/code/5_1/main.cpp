#include <string>
#include <iostream>
using namespace std;
int main()
{   
    char s[101];
    char signs[] = { '.', ',', '!', '?', ';', ':', '-' };
    cin.getline(s, 101); // не более 100 символов c учётом'\0'
    int count = 0;
    for (int i = 0; i < 100; i++) {
        for (size_t k = 0; k < sizeof(signs); k++) {
            if (s[i] == signs[k]) {
                count++;
            }
        }
    }
    cout << count;
}
