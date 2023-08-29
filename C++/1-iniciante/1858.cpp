#include <iostream>

using namespace std;

#define MAX 20

int main() {
    int n, t, menor = MAX, pos = 0;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> t;
        if (t < menor) {
            menor = t;
            pos = i;
        }
    }
    cout << pos << endl;
    return 0;
}