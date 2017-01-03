#include <cmath>
#include <iostream>

using namespace std;

int main()
{
	int n;
	cin >> n;
	int days = 0;
	int factory = 1;

	int without_fact = ceil((factory + sqrt(factory * factory + 8 * n * factory)) / (2 * factory));
	int with_fact = ceil((2 * factory + sqrt(4 * factory * factory + 16 * n * factory)) / (4 * factory) + 1);

	while (with_fact < without_fact)
	{
		factory *= 2;
		++days;
		without_fact = ceil((factory + sqrt(factory * factory + 8 * n * factory)) / (2 * factory));
		with_fact = ceil((2 * factory + sqrt(4 * factory * factory + 16 * n * factory)) / (4 * factory) + 1);
	}

	days += ceil((factory + sqrt(factory * factory + 8 * n * factory)) / (2 * factory));
	cout << days << endl;
	return 0;
}
