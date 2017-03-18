#include <iostream>
#include <sstream>
#include <set>
#include <string>
#include <vector>

using namespace std;

int main()
{
	set<string> numbers_fixed;
	vector<string> numbers_raw;
	int n;
	cin >> n;
	for (int i = 0; i < n; ++i)
	{
		string m;
		cin >> m;
		numbers_raw.push_back(m);
		if (m.find("??") == string::npos && !numbers_fixed.insert(m).second)
		{
			cout << "No" << endl;
			exit(0);
		}
	}

	for (string& num : numbers_raw)
	{
		if (num.find("??") != string::npos)
		{
			bool found = false;
			for (int i = 0; i < 10 && !found; ++i)
				for (int j = 0; j < 10 && !found; ++j)
				{
					ostringstream buf;
					buf << num[0] << i << j << num[3] << num[4] << num[5] << num[6];
					found = numbers_fixed.insert(buf.str()).second;
					cout << "inserted: " << buf.str() << endl;
				}
			if (!found)
			{
				cout << "No" << endl;
				exit(0);
			}
		}
	}
	
	cout << "Yes" << endl;
	for (string& num : numbers_raw)
		cout << num << endl;
}
