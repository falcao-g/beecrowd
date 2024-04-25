#include <iostream>

using namespace std;

int main() {
    int l, n;
    cin >> l >> n;

    long long int um = n - 1;
    long long int maior = l - um;
    long long int ans = (maior * maior) + (n - 1);

    cout << ans << endl;
}
