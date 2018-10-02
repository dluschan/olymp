#include <iostream>

using namespace std;

int main()
{
	int n, d, m;
	cin >> n >> d >> m;
	for (int i = 0; i < m; ++i)
	{
		int x, y;
		cin >> x >> y;
		cout << ((abs(x - y) <= d && abs(x + y - n) <= n - d) ? "YES" : "NO") << endl;
	}
	return 0;
}
