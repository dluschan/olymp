#include <iostream>

using namespace std;

int gcd(int a, int b) { return (b) ? gcd(b, a % b) : a; }

int main()
{
	int a, b, c, d;
	std::cin >> a >> b >> c >> d;
	int i = 0;
	while (a * d < c * b)
	{
		++a;
		++b;
		int vGcd = gcd(a, b);
		a /= vGcd;
		b /= vGcd;
		++i;
	}
	cout << ((a * d > c * b) ? 0 : i) << endl;
	return 0;
}
