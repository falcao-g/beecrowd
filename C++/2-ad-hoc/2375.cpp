#include <iostream>

using namespace std;

#define yes cout << "S" << endl
#define no cout << "N" << endl


int main() {
	int d;
	cin >> d;

	int a, l, p;
	cin >> a >> l >> p;

	if (d <= a && d <= l && d <= p)
		yes;
	else
		no;

	return 0;
}
