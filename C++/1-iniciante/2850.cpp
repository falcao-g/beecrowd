#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false); cin.tie(0);

    map<string, string> m;

    m.insert(pair<string, string>("esquerda", "ingles"));
    m["direita"] = "frances";
    m["nenhuma"] = "portugues";
    m["as duas"] = "caiu";

    string s;
    while (getline(cin, s)) {
        cout << m[s] << "\n";
    }
}
