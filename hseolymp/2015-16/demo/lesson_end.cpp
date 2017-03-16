#include <iostream>

using namespace std;

int main()
{
	int k;
	cin >> k;
	const int m = (k - 1) * 5 + k * 45;
	cout << m / 60 + 8 << ' ' << m % 60 << endl;
	return 0;
}
