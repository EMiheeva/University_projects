#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;
const int SIZE = 1000;
int main()
{
    ifstream text;
    ofstream out;
    int a[SIZE];
    int count = 0; //счётчик
    if (!text) {
        cout << "Add input.txt!" << endl;
    }
    else {
        cout << "input.txt is exist!" << endl;
        text.open("input.txt");
    }
    out.open("output");
    int N;
    string s;
    text >> N;
    
    while (!(text.eof())) {
        text >> s;
        a[count] = s.length();
        count++;
    }
    
    int k = 0;
    while (k < N) {
        int minim = INT_MAX;
        int index = 0;
        for (int i = 0; i < count; ++i) {
            if (a[i] < minim) {
                minim = a[i];
                index = i;
            }
        }
        if (minim == INT_MAX) break;

        a[index] = INT_MAX;

        text.open("input.txt");
        text >> s;
        for (int i = 0; i <= index; ++i)
            text >> s;
        int n = 0;
        for (int i = 0; i < s.length(); ++i) {
            for (int j = i+1; j < s.length(); ++j) {
                if (s[i] == s[j]) {
                    n++;
                }
            }
            if (n == 2) {
                k++;
                out << s << " ";
            }
        }
        text.close();
    }
    cout << "Program done! Check outut.txt!" << endl;
    return 0;
}



