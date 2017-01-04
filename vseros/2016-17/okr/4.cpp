#include <iostream>

int main()
{
	int n, p, k;
	cin >> n >> p >> k;

	int pos1 = (p + 2 * k * (p % 2 * 2 - 1)) % n + 1;
	int pos2 = (p - 2 + 2 * k * (p % 2 * 2 - 1)) % n + 1;
	cout << min(pos1, pos2) << ' ' << max(pos1, pos2) << endl;
}
