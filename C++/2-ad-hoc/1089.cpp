#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false); cin.tie(0);

    int n;
    cin >> n;
    while (n != 0) {
        int v[n];
        for (int i = 0; i < n; i++) {
            cin >> v[i];
        }
        int picos = 0;

        for (int m = 0; m < n; m++) {
            int antecessor = (m-1 < 0) ? n-1 : m-1;
            int sucessor = (m+1 >= n) ? 0 : m+1;

            if (v[antecessor] > v[m] && v[m] < v[sucessor]) {
                picos += 1;
                    continue;
            }

            if (v[antecessor] < v[m] && v[m] > v[sucessor]) {
                picos += 1;
                    continue;
            }
        }

        cout << picos << "\n";
        cin >> n;
    }

    return 0;
}
