#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        int x, soma;
        cin >> x;

        if (x % 2 == 0) {
            soma = 0;
        } else {
            soma = 1;
        }

        cout << soma << '\n';
    }
}