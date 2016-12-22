#include <iostream>

using namespace std;

int main()
{
	int p = 0;

	int n;
	cin >> n;

	int a[n], b[n], c[n];
	for (int i = 0; i < n; ++i)
		cin >> a[i] >> b[i] >> c[i];

	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j)
		{
			int k = 0;
			if (a[i] == a[j])
				++k;
			if (b[i] == b[j])
				++k;
			if (c[i] == c[j])
				++k;
			if (k == 1)
				++p;
		}

	cout << p / 2 << endl;
	return 0;
}
