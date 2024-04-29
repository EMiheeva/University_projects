#include <iostream>

int main() {
    
    int n;
    double x;
    double product = 1.0;
    int min_idx = -1;
    double min_el = 0;
    std::cin >> n;
    for (int i = 0; i < n; i++) {
        std::cin >> x;

        if (x < 0 && fabs(x - round(x)) > 0) 
        {
            product *= x;
            if (min_el > x) {
                min_el = x;
                min_idx = i;
            }
        }
    }

    if (min_idx != -1) {
        std::cout << "product: " << product << std::endl;
        std::cout << "min el: " << min_el << std::endl;
        std::cout << "min idx: " << min_idx << std::endl;
    }
    else
    {
        std::cout << "no elements" << std::endl;
    }

    return 0;
}
