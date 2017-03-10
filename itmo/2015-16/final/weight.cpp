#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	int n;
	cin >> n;
	int weight[n];
	int diff = 0;
	for (int i = 0; i < n; ++i)
	{
		int sign;
		cin >> weight[i] >> sign;
		if (sign == 2) 
			weight[i] *= -1;
		diff += weight[i];
	}

	int min_diff = abs(diff);
	for (int i = 0; i < n; ++i)
	{
		for (int j = i + 1; j < n; ++j)
			if (abs(diff - 2*(weight[i] + weight[j])) < min_diff)
				min_diff = abs(diff - 2*(weight[i] + weight[j]));

		if (abs(diff - 2*weight[i]) < min_diff)
			min_diff = abs(diff - 2*weight[i]);
	}

	cout << min_diff << endl;
	return 0;
}
