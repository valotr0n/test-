#include <iostream>
#include <cmath>
using namespace std;
int main() {
    int n;
    float  x,s = 0.0, fact = 1;
    cout << "Enter n: ";
    cin >> n;
    cout << "Enter x: ";
    cin >> x;
    for (int i = 1; i <= n; ++i) {
        fact *= i;
        double calculate = pow(x,i)/fact;
        s += calculate;
    }
    cout << "sum = " << s << endl;
    return 0;
}