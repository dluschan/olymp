#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int orders[n];
    for(int i = 0; i < n; ++i)
        cin >> orders[i];

	sort(&orders[0], &orders[n]);

	int res = 1;
	for(int i = 0; i < n; ++i)
		res *= (orders[i] - i);

    cout << res << endl;
    return 0;
}
