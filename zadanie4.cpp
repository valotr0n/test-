#include <iostream>
#include <cmath>
using namespace std;

int main() {
    float mass, height, imt;
    cout << "Enter your mass: ";
    cin >> mass;
    cout << "Enter your height in metres: ";
    cin >> height;
    imt = (mass)/pow(height,2);
    cout << "Your imt = " << imt << endl;


    if (imt < 18.5) {
        cout << "Insufficient imt" << endl;
        } else if (18.5 <= imt < 25) {
            cout << "Normal imt" << endl;
           } else if (25 <= imt < 30) {
                cout << "Excess imt" << endl;
                } else {
                    cout << "Obesity" << endl; 
                }
}
               