#include <iostream>
#include <map>

using namespace std;

int main()
{
	map<int, int> blocks;
	int n;
	cin >> n;
	int sum = 0;
	for (int i = 0; i < n; ++i)
	{
		int w, h;
		std::cin >> w >> h;
		if (blocks[w] < h)
		{
			sum += h - blocks[w];
			blocks[w] = h;
		}
	}
	cout << sum << endl;

	return 0;
}
