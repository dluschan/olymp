#include <iostream>
#include <string>
#include <map>
#include <vector>

using namespace std;

int main()
{
	int trash;
	cin >> trash;
	string s;
	cin >> s;
	map<char, int> coord = {('L', 0), ('R', 0), ('D', 1), ('U', 1)};
	map<char, int> sign = {('L', -1), ('R', 1), ('D', -1), ('U', 1)};
	vector<int> dir = {0, 0};
	int dots = 1;
	for (char c: s)
	{
		if (dir[coord[c]] * sign[c] < 0)
		{
			++dots;
			dir[(coord[c] + 1) % 2] = 0;
		}
		dir[coord[c]] = sign[c];
	}
	cout << dots << endl;
}
