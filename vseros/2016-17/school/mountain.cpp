#include <iostream>

using namespace std;

int main()
{
	int n;
	cin >> n;

	int up = 0;
	int prev = 0;
	int minfinish = 1;
	int minstart = 1;
	int start, finish;

	int top;
	cin >> top;

	for(int i = 2; i < n + 1; ++i)
	{
	    prev = top;
		cin >> top;

	    if (up == 1)
		{
	        if (top > prev)
	            start = i - 1;

	        if (top < prev)
			{
	            finish = i;
	            up = 0;
	            if (minfinish - minstart == 0 or finish - start < minfinish - minstart)
				{
	                minfinish = finish;
	                minstart = start;
				}
			}
		}

	    if (up == 0 && top > prev)
		{
            start = i - 1;
            up = 1;
		}
	}

	if (minfinish - minstart == 0)
	    cout << 0 << endl;
	else
	    cout << minstart << " " << minfinish << endl;
	
	return 10;
}
