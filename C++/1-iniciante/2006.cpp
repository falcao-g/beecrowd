#include <iostream>

using namespace std;

int main() {
	ios::sync_with_stdio(false); cin.tie(0);
	int correto;
	int resposta = 0;
	cin >> correto;

	int c;
	for (int i = 0; i <= 4; i++) {
		cin >> c;
		if (c == correto) {
			resposta += 1;
		}
	}

	cout << resposta << "\n";

	return 0;
}