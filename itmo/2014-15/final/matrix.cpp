#include <iostream>

std::pair<int, int> process(int x)
{
	int dx = 0;
	int dy = 0;
	for (int i = 1; i <= 5; ++i)
		for (int j = 1; j <= 5; ++j)
		{
			if (x % 2 && i != j)
			{
				dx += i*(j - i)/abs(i - j);
				dy += j*(i - j)/abs(i - j);
			}
			x /= 2;
		}
	return std::make_pair(dx, dy);
}

int main()
{
	const std::pair<int, int> pattern = std::make_pair(-1, -1);
	int n = 0;
	for (int k = 0; k < 32*1024*1024; ++k)
	{
		if (process(k) == pattern)
			++n;
	}
	std::cout << n << std::endl;
}
