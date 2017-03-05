#include <iostream>

using namespace std;

int clumsy()
{
	int n;
	cin >> n;

	int a[n], b[n], c[n];
	for (int i = 0; i < n; ++i)
		cin >> a[i] >> b[i] >> c[i];

	int couples = 0;
	for (int i = 0; i < n; ++i)
		for (int j = i + 1; j < n; ++j)
		{
			int k = 0;
			if (a[i] == a[j])
				++k;
			if (b[i] == b[j])
				++k;
			if (c[i] == c[j])
				++k;
			if (k == 1)
				++couples;
		}

	return couples;
}

int main()
{
	cout << clumsy() << endl;
	return 0;
}
