#include <iostream>
using namespace std;

int main(){
    int x, y, x1, y1, halfsum, dubleproz;
    cout << "Enter x: ";
    cin >> x;
    cout << "Enter y: ";
    cin >> y;
    halfsum = (x+y)/2;
    dubleproz = 2*(x*y);

    if (x<y) {
        x1 = halfsum;
        y1 = dubleproz;
    } else if (y<x) {
        x1 = dubleproz;
        y1 = halfsum;
    }
    cout << "New x :" << x1 << endl;
    cout << "New y :" << y1 << endl;
    return 0;

}