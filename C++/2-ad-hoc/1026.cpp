#include <iostream>

using namespace std;

int main() {
  ios::sync_with_stdio(false); cin.tie(0);

  long int num1, num2;
  while (cin >> num1 >> num2) {
    cout << (num1 ^ num2) << "\n";
  }
}
