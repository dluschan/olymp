#include <iostream>
#include <string>

using namespace std;

string calculate_route(int num, char minus, char plus, char skip)
{
	string route = "";
	while (num != 0)
	{
		int c = num % 3;
		num /= 3;
		if (c == 2)
		{
			route += minus;
			num += 1;
		}
		else
			if (c == 1)
				route += plus;
			else
				route += skip;
	}
	return route;
}

int main()
{
	int x1, y1, x2, y2;
	cin >> x1 >> y1 >> x2 >> y2;

	string route_x = calculate_route(x2 - x1, 'l', 'r', 's');
	string route_y = calculate_route(y2 - y1, 'd', 'u', 's');

	while (route_x.length() != route_y.length())
		if (route_x.length() < route_y.length())
			route_x += 's';
		else
			route_y += 's';

	string res = "";
	for (unsigned int i = 0; i < route_x.length(); ++i)
	{
		if (route_x[i] == 's' or route_y[i] == 's')
			res += (route_x[i] != 's') ? route_x[i] : route_y[i];
		else
		{
			cout << "no" << endl;
			return 0;
		}
	}
	cout << "yes" << endl;
	cout << res << endl;
}
