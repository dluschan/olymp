#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	int n, m;
	cin >> n >> m;
	vector<int> p(n);
	int sum = 0;
	for (int i = 0; i < m; ++i)
	{
		string str;
		cin >> str;

		int pos = str.find('+');
		if (pos != string::npos && str.find('+', pos + 1) == string::npos)
		{
			++p[pos];
			++sum;
		}
	}

	for (int party = 0; party < n; ++party)
		if (p[party] * 100 >= 7 * sum)
			cout << party + 1 << " ";
	cout << endl;

	return 0;
}
