#include <iostream>
using namespace std;
int main() {
    int i;
    unsigned long long p = 1;
    for (i = 1; i<= 50; ++i) {
        if (i % 3 == 0) {
            p *= i;
        }
    } 
    cout << "proizvedenit chisel kratnix 3 v diapazone [1,50] = " << p << endl;
    return 0;
}