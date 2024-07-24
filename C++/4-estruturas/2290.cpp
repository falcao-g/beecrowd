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

        vector<long long int> resp(2);
        int k = 0;
        long long int j = 0;
        while (j < n) {
            if (j == n-1) {
                resp[1] = numeros[j];
                break;
            }

            if ((numeros[j] ^ numeros[j+1]) == 0) {
                j += 1;
            } else {
                resp[k] = numeros[j];
                k += 1;
                if (j == n - 2) {
                    resp[1] = numeros[j+1];
                    break;
                }
            }
            j += 1;
        }

        sort(resp.begin(), resp.end(), compara);

        cout << resp[0] << " " << resp[1] << "\n";

    }
}
