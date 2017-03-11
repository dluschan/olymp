#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int size[n][4];
    for (int i = 0; i < n; ++i)
    {
		size[i][0] = i + 1;
        cin >> size[i][1] >> size[i][2] >> size[i][3];
    }
	
    for (int i = 0; i < n - 1; ++i)
	    for (int j = 0; j < n - 1 - i; ++j)
			if (size[j][1] + size[j][2] + size[j][3] < size[j+1][1] + size[j+1][2] + size[j+1][3])
				swap(size[j], size[j+1]);
	
	bool fit = true;
    for (int i = 0; i < n - 1; ++i)
		if (!(size[i][1] > size[i+1][1] && (size[i][2] > size[i+1][2] && size[i][3] > size[i+1][3]) || (size[i][2] > size[i+1][3] && size[i][3] > size[i+1][2])))
			fit = false;
	
	if (fit)
	{
	    for (int i = 0; i < n; ++i)
			cout << size[i][0] << ' ';
		cout << endl;
	}
	else
		cout << -1 << endl;
	
    return 0;
}
