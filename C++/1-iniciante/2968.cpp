#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int v, n, m, x;
    cin >> v >> n;
    m = v * n;
    for (int i = 1; i <= 9; i++) {
        x = (m * i) / 10;
        if ((m * i) % 10 != 0)
            x++;
        cout << x;
        if (i < 9)
            cout << " ";
    }
    cout << endl;
}