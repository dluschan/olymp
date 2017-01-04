#include <iostream>
#include <set>

int main()
{
	int n;
	cin >> n;
    multiset<int> old_prices;
	for (int i = 0; i < n; ++i)
	{
		int price;
		cin >> price;
		if (old_prices.count(price)) //старая ли это цена
			old_prices.erase(price);
		else
		{
			cout << price << endl;
			old_prices.insert(price * 4 / 3);
		}
	}
}
