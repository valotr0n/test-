#include <iostream>
#include <cmath>
using namespace std;
int main() {
    double nachalo = -4.0, shag = 0.2, konec = 4.2;
    while (nachalo <= konec) 
    {
        double calculate = cos(nachalo)/(2+nachalo);
        cout << "znachenie = " << nachalo << " output = " << calculate << endl;
        nachalo += shag;

    }
    return 0;
}
