#include <iostream>
#include <set>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int boss[n];
	boss[0] = 0;
    for(int i = 1; i < n; ++i)
        cin >> boss[i];
	
    int x;
    cin >> x;
	set<int> out;
	out.insert(x);
	
    for(int i = 0; i < n; ++i)
        if (out.count(boss[i]))
			out.insert(i+1);

	cout << out.size() << endl;
    return 0;
}
