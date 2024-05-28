#include <bits/stdc++.h>
#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false); cin.tie(0);

    int n; cin >> n;
    vector<int> v;

    for (int i = 0; i < n; i++) {
        int k;
        cin >> k;
        v.push_back(k);
    }

    int alv; cin >> alv;
    int atual = 0;
    int esq = 0;
    int dir = n - 1;

    while (atual != alv) {
        atual = v[esq] + v[dir];

        if (atual < alv) {
            esq += 1;
        } else if (atual > alv) {
            dir -= 1;
        }
    }

    cout << v[esq] << " " << v[dir] << "\n";

    return 0;
}
