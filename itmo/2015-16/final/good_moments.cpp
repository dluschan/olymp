#include <iostream>
#include <sstream>
#include <string>

using namespace std;

int main()
{
	int a, b, x, y, z, h1, m1, s1, h2, m2, s2;
	char c;
	cin >> a >> b >> x >> y >> z >> h1 >> m1 >> s1 >> h2 >> m2 >> s2 >> c;

	const int day = x*a*b + y*b + z;
	const int start_time = h1*a*b + m1*b + s1;
	const int finish_time = h2*a*b + m2*b + s2;
	bool need_next_day = (start_time > finish_time) ? true : false;
	int good_moments = 0;

	for (int t = start_time; need_next_day || !need_next_day && t != finish_time + 1;)
	{
		int h = t / (a*b);
		if (x > 9 && h < 10)
			h *= 10;

		int m = t % (a*b) / b;
		if (a > 9 && m < 10)
			m *= 10;

		int s = t % b;
		if (b > 9 && s < 10)
			s *= 10;

		ostringstream st;
		st << h << m << s;

		if (st.str().find(c) != string::npos)
			++good_moments;

		if (++t == day)
			need_next_day = false;
		t %= day;
	}
	cout << good_moments << endl;
	return 0;
}
