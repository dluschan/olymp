#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int n, k;
	cin >> n >> k;

	vector<int> b;
	b.push_back(0);
	for (int i = 0; i < n; ++i)
	{
		int m;
		cin >> m;
		b.push_back(i ? b[i] + m : m);
	}

	vector<int> left;
	vector<int> right(n - k + 1);
	vector<int> top;

	for (int i = 0; i < n - k + 1; ++i)
		left.push_back((i < k) ? 0 : max(left[i - 1], b[i] - b[i - k]));
	for (int i = n - k; i >= 0; --i)
		right[i] = (i > n - k - k) ? 0 : max(right[i + 1], b[i + k + k] - b[i + k]);
	for (int i = 0; i < n - k + 1; ++i)
		top.push_back(max(left[i], right[i]));
	cout << *min_element(top.begin(), top.end()) << endl;
	
	return 0;
}
