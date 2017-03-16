#include <iostream>

using namespace std;

int main()
{
	int n, m, k;
	cin >> n >> m >> k;
	cout << (k < 3 || m < (n + k - 3) / (k - 2) * 2 ? 0 : (n + m + k - 1) / k) << endl;
	return 0;
}
