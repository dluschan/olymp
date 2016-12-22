#include <iostream>

using namespace std;

int main()
{
	int h, w;
	cin >> h >> w;
	bool sea = true;
	int shore = 0;
	int res = 0;

	for (int i = 0; i < h; ++i)
	{
		for (int j = 0; j < w; ++j)
		{
			char c;
			cin >> c;
			if (c == '.')
				res += (sea) ? 0 : 1;
			if (c == '/' || c == '\\')
			{
				++shore;
				sea = !sea;
			}
		}
	}
	res += shore / 2;
	cout << res << endl;
	return 0;
}
