//Окружной этап всероссийской олимпиады школьников по информатике Москва, 14 декабря 2014 г.
//Задача 5. Строки

#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	vector<int> n[3];
	string s[3];

	s[0] = "azzaaaa";
	s[1] = "aazzaa";
	s[2] = "azzza";

	for (int i = 0; i < 3; ++i)
	{
		n[i].push_back(1);
		int index = 1;
		while (index < s[i].length())
		{
			if (s[i][index] == s[i][index - 1])
			{
				s[i].erase(index, 1);
				++n[i][index - 1];
			}
			else
			{
				n[i].push_back(1);
				++index;
			}
		}
	}
	for (int i = 0; i < 3; ++i)
	{
		for (int j = 0; j < s[0].length(); ++j)
			cout << s[i][j] << '\t';
		cout << endl;
		for (int j = 0; j < s[0].length(); ++j)
			cout << n[i][j] << '\t';
		cout << endl;
	}

	if (s[0] != s[1] || s[1] != s[2])
	{
		cout << 0;
	}
	else
	{
		for (int i = 0; i < s[0].length(); ++i)
		{
			int medium =
				n[0][i] + n[1][i] + n[2][i] - max(n[0][i], max(n[1][i], n[2][i])) - min(n[0][i], min(n[1][i], n[2][i]));
			for (int p = 0; p < medium; ++p)
				cout << s[0][i];
		}
		cout << endl;
	}
	return 0;
}
