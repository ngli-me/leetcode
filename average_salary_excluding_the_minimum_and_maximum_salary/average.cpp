#include <iostream>
#include <stdlib.h>
#include <vector>

double average(std::vector<int>& salary) {
    auto sum = 0;
    // Since unique, and l >= 3, can just set it as first number instead of using floor and ceil
    auto min = salary[0], max = salary[0];
    for (auto s : salary) {
        if (s < min)
            min = s;
        else if (s > max) 
            max = s;
        sum += s;
    }
    sum -= (min + max);
    return ((double)sum)/(salary.size() - 2); 
}

void print_vec(std::vector<int>& salary) {
    for (auto s : salary) {
        std::cout << s << " ";
    }
    std::cout << std::endl;
}

int main() {
    std::vector<int> v = {4000,3000,1000,2000};
    print_vec(v);
    std::cout << average(v) << std::endl;
    // std::cout << "Hello World!";
    return 0;
}
