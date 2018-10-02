#include <iostream>

using namespace std;

int main()
{
	long long int n, m, k;
	cin >> n >> m >> k;
	if (2*n*m % k)
	{
		cout << "NO" << endl;
	}
	else
	{
		cout << "YES" << endl;
		cout << 0 << ' ' << 0 << endl;
		cout << n << ' ' << 1 << endl;
		cout << n * ((2*m + k - 1) / k) - 2*n*m / k << ' ' << (2*m + k - 1) / k << endl;
	}
	return 0;
}
