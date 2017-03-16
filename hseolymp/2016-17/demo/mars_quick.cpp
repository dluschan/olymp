#include <iostream>

using namespace std;

int main()
{
	int n;
	cin >> n;
	if (n == 1)
		cout << 2 << endl;
	else
	{
		int days = 3;
		int water = 3;

		while (water >= n)
		{
			water *= 2;
			++days;
		}
		cout << days << endl;
	}
}
