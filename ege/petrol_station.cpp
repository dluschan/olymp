#include <iostream>
#include <string>

using std::cin;
using std::cout;
using std::endl;
using std::string;

int main()
{
	int n;
	cin >> n;
	string company1, company2, street1, street2;
	int count1 = 0;
	int count2 = 0;
	int price1 = 4000;
	int price2 = 4000;
	for (int i = 0; i < n; ++i)
	{
		string company, street;
		int mark, price;
		std::cin >> company >> street >> mark >> price;
		if (mark != 92)
			continue;

		if (price < price1)
		{
			price2 = price1;
			company2 = company1;
			street2 = street1;
			count2 = count1;

			price1 = price;
			company1 = company;
			street1 = street;
			count1 = 1;
			continue;
		}

		if (price == price1)
		{
			++count1;
			continue;
		}

		if (price < price2)
		{
			price2 = price;
			company2 = company;
			street2 = street;
			count2 = 1;
			continue;
		}

		if (price == price2)
		{
			++count2;
			continue;
		}
	}
	if (count2 > 1)
	{
		cout << count2 << endl;
	}
	if (count2 == 1)
	{
		cout << company2 << ' ' << street2 << endl;
	}
	if (count2 == 0 and count1 > 1)
	{
		cout << count1 << endl;
	}
	if (count2 == 0 and count1 == 1)
	{
		cout << company1 << ' ' << street1 << endl;
	}
	return 0;
}
