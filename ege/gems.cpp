#include <iostream>
#include <vector>

using namespace std;

int main()
{
	vector<int> gems(20, 0);
	int n;
	cin >> n;
	double k = 0.05 * n;
	int m = 0;
	for (int i = 0; i < n; ++i)
	{
		string trash;
		int w;
		cin >> trash >> trash >> w;
	    ++gems[20-w];
	}
	int i = 0;
	int prev = 20;
	int cur = 20;
	while (m < k)
	{
	    if (gems[i] > 0)
		{
	        prev = cur;
	        cur = i;
		}
	    m += gems[i++];
	}
	int total = 0;
	for_each(gems.begin(), ++++++++++gems.begin(), [&total](int x) { total += x; });
	cout << ((total >= k || m == k) ? 20 - i + 1 : 20 - prev) << endl;
}
