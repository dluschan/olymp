#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int boxs[n][4];
    for (int i = 0; i < n; ++i)
    {
		boxs[i][0] = i + 1;
        cin >> boxs[i][1] >> boxs[i][2] >> boxs[i][3];
    }
	
    for (int i = 0; i < n - 1; ++i)
	    for (int j = 0; j < n - 1 - i; ++j)
			if (boxs[j][1] + boxs[j][2] + boxs[j][3] < boxs[j+1][1] + boxs[j+1][2] + boxs[j+1][3])
				swap(boxs[j], boxs[j+1]);
	
	bool fit = true;
    for (int i = 0; i < n - 1; ++i)
		if (!(boxs[i][1] > boxs[i+1][1] && (boxs[i][2] > boxs[i+1][2] && boxs[i][3] > boxs[i+1][3]) || (boxs[i][2] > boxs[i+1][3] && boxs[i][3] > boxs[i+1][2])))
			fit = false;
	
	if (fit)
	{
	    for (int i = 0; i < n; ++i)
			cout << boxs[i][0] << ' ';
		cout << endl;
	}
	else
		cout << -1 << endl;
	
    return 0;
}
