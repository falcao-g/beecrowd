#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, x, c = 0;

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> x;
        if (x != 1)
            c++;
    }
    cout << c << '\n';
}