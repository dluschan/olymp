#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int a = 2;
	int b = 162;
	//cin >> a >> b;
	vector<int> proc;
	proc.push_back(b);
	
	while (a != b)
	{
		switch (b % 10)
		{
		case 0:
		case 2:
		case 4:
		case 6:
		case 8:
			b /= 2;
			proc.push_back(b);
			break;
		case 1:
			b /= 10;
			proc.push_back(b);
			break;
		default:
			cout << "No" << endl;
			return 0;
		}
	}

	cout << "Yes" << endl;
	cout << proc.size() << endl;
	for (int i = proc.size() - 1; i >= 0; --i)
		cout << proc[i] << " ";
	cout << endl;
	return 0;
}
