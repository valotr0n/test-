#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int  x , areaSqrt, areaCircle, area, pi = 3.14;
    cout << "Введите значение x: ";
    cin >> x;
    areaSqrt = x * x;
    areaCircle = pi * double(x/2);
    area = areaSqrt - areaCircle;
    cout << "Area Squarte = " << areaSqrt << endl;
    cout << "Area Circle = " << areaCircle << endl;
    cout << "Area = " << area << endl;
    return 0;
    
}