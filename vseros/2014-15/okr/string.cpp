#include <iostream>
#include <string>
#include <vector>

using namespace std;

int medium(int a, int b, int c) { return a + b + c - min(a, min(b, c)) - max(a, max(b, c)); }

int main()
{
	const int n = 3;
	string s[3];
	vector<int> v[3];
	for (int i = 0; i < n; ++i)
	{
		cin >> s[i];
		v[i].push_back(1);
		for (size_t j = 1; j < s[i].length();)
		{
			if (s[i][j] == s[i][j - 1])
			{
				++v[i][j - 1];
				s[i].erase(j, 1);
			}
			else
			{
				v[i].push_back(1);
				++j;
			}
		}
	}
	if (s[0] == s[1] and s[1] == s[2])
	{
		for (size_t i = 0; i < s[0].length(); ++i)
		{
			medium(v[0][i], v[1][i], v[2][i]);
			for (int j = 0; j < medium(v[0][i], v[1][i], v[2][i]); ++j)
				cout << s[0][i];
		}
		cout << endl;
	}
	else
	{
		cout << ("IMPOSSIBLE") << endl;
	}
}
