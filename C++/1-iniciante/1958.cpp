#include <iostream>

using namespace std;

int main() {
    double n;
    cin >> n;

    cout.precision(4);
    cout << scientific << showpoint << showpos << uppercase << n << endl;
}