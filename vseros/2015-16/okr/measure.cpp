#include <iostream>

using namespace std;

int main()
{
	int s, a, p, v;
	v = 103;

	p = v / 4;
	v %= 4;

	a = p / 4;
	p %= 4;

	s = a / 3;
	a %= 3;

	cout << s << " " << a << " " << p << " " << v << endl;
	return 0;
}
