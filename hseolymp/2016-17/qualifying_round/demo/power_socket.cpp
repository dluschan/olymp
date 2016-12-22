#include <iostream>

int main()
{
	int n, m, a, b;
	std::cin >> n >> m >> a >> b;
	std::cout << ((4*a < b) ? (m - n) * a : (m - n) / 4 * b + std::min((m - n) % 4 * a, b)) << std::endl;
	return 0;
}
