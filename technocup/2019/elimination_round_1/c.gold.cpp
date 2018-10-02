#include <iostream>
#include <numeric>
#include <vector>

using namespace std;

bool check(const vector<int>& s, int i, int k)
{
    if (i == s.size())
        return true;
	int g = 0;
	for (; i < s.size(); ++i)
	{
		g += s[i];
		if (g == k)
            return check(s, i+1, k);
		if (g > k)
            return false;
	}
	return false;
}

bool fit(const vector<int>& s, int p)
{
	int b = 0;
	for (int i = 0; i < s.size() - 1; ++i)
	{
		b += s[i];
        if (p % b == 0 && check(s, 0,  b))
            return true;
	}
    return false;
}

int main()
{
	int n;
	cin >> n;
	vector<int> s;
	s.reserve(n);
	int q = 0;
	for (int i = 0; i < n; ++i)
	{
		char c;
		cin >> c;
		int x = c - '0';
		if (x)
		{
			q += x;
			s.push_back(x);
		}
	}
	cout << ((s.size() == 0 || fit(s, q)) ? "YES" : "NO") << endl;
}
