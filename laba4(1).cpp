#include <iostream>
#include <cmath>
using namespace std;

int main() {
    float x, r, lambd, firstcal, secondcal, result;
    cout << "Enter x: ";
    cin >> x;
    cout << "Enter r: ";
    cin >> r;
    cout << "Enter lambd: ";
    cin >> lambd;

    firstcal = 2/double(x);
    secondcal = x - (lambd/r);
    double thirdcal = pow(pow(x - lambd, 2), 1.0/3.0) - pow(lambd, 2);;
    result = firstcal * (secondcal/thirdcal);
    cout << "rusult = " << result << endl;
    return 0;
    
}