#include <iostream>

using namespace std;

int main()
{
	int n;
	cin >> n;
	for(int i = 0; i < n; ++i)
	{
		int a, b, c, d;
		cin >> a >> b >> c >> d;
		cout << ((a + b*c <= d) ? "YES" : "NO") << endl;
	}
	return 0;
}
