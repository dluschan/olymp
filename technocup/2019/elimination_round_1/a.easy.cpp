#include <iostream>

using namespace std;

bool iseasy(int n)
{
	for (int i = 0; i < n; ++i)
	{
		int x;
		cin >> x;
		if (x == 1)
			return false;
	}
	return true;
}

int main()
{
	int n;
	cin >> n;
	cout << ((iseasy(n)) ? "EASY" : "HARD") << endl;
	return 0;
}
