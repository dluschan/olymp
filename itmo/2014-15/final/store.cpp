#include <cmath>
#include <iostream>

int main()
{
	for (int x = 1; x < 100; ++x)
		std::cout << x << ' ' << ceil(log(x*10000000+2563218)/log(2)) - ceil(log(256*32*18*x)/log(2)) << std::endl;
}
