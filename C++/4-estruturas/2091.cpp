#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool compara(long long int a, long long int b) {
    return a < b;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(0);

    long long int n;
    while (cin >> n) {
        if (n == 0) {
            break;
        }

        vector<long long int> numeros(n, 0);
        for (long long int i = 0; i < n; i++) {
            cin >> numeros[i];
        }

        sort(numeros.begin(), numeros.end(), compara);

        long long int resp = 0;
        long long int j = 0;
        while (j < n) {
            if (j == n-1) {
                resp = numeros[j];
                break;
            }

            if ((numeros[j] ^ numeros[j+1]) == 0) {
                j += 1;
            } else {
                resp = numeros[j];
            }
            j += 1;
        }

        cout << resp << "\n";

    }
}
