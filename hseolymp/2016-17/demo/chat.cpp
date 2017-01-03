#include <iostream>
#include <string>

int main()
{
	int n, days = 1;
	std::cin >> n;

	std::string date_prev, date_cur;
	std::cin >> date_prev;
	for (int i = 1; i < n; ++i)
	{
		std::cin >> date_cur;
		if (date_prev >= date_cur)
			++days;
		date_prev = date_cur;
	}
	std::cout << days << std::endl;

	return 0;
}
