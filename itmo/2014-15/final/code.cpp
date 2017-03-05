#include <iostream>
#include <stack>
#include <algorithm>

using namespace std;

int clumsy()
{
	string res = "";
	for(int i = 1; i < 1000; ++i)
	{
		int copy_num = i;
		stack<int> digits;
		while(copy_num)
		{
			digits.push(copy_num % 2);
			copy_num /= 2;
		}
		while(!digits.empty())
		{
			res += digits.top() ? '1' : '0';
			digits.pop();
		}
	}
	return res.find("111111111") + 1;
}

int artful()
{
	int number = 1;
	int ordered_ones = 0;
	int sum_digits = 0;
	while(ordered_ones != 9)
	{
		int copy_num = number;
		stack<int> digits;
		while(copy_num)
		{
			digits.push(copy_num % 2);
			copy_num /= 2;
		}
		while(!digits.empty())
		{
			++sum_digits;
			if (digits.top())
			{
				++ordered_ones;
				if (ordered_ones == 9)
					break;
			}
			else
				ordered_ones = 0;	
			digits.pop();
		}
		++number;
	}
	return sum_digits - 8;
}

int main()
{
	cout << clumsy << endl;
	cout << artful << endl;
	return 0;
}
