#include <iostream>

using namespace std;

int number_of_bits(int number) {
  int count = 0;
  while (number > 0) {
    number >>= 1;
    count++;
  }
  return count;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(0);
    int n;
    while (cin >> n) {
        cout << number_of_bits(n) -1 << "\n";
    }
}
