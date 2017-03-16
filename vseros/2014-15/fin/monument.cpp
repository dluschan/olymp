#include <iostream>
#include <fstream>
#include <climits>

using namespace std;

int dir(int x1, int y1, int x2, int y2)
{
    if (x1 == x2)
        return (y2 > y1) ? 1 : -1;
    else
        return 0;
}

int main()
{
    int n;
    int k;

    ifstream fin("input2.txt");
    fin >> n >> k;
    int a[n+1][2];
    int ymax = -1;
    int ymin = 1000001;
    int xmax = -1;
    int xmin = 1000001;
    for (int i = 0; i < n; ++i)
    {
        fin >> a[i][0] >> a[i][1];
        if (a[i][1] > ymax)
            ymax = a[i][1];
        if (a[i][1] < ymin)
            ymin = a[i][1];
        if (a[i][0] > xmax)
            xmax = a[i][0];
        if (a[i][0] < xmin)
            xmin = a[i][0];
    }
    fin.close();
    a[n][0] = a[0][0];
    a[n][1] = a[0][1];

    int lines = ymax - ymin;
    int b[lines][2];
    for (int i = 0; i < n; ++i)
    {
        int x1 = a[i][0];
        int y1 = a[i][1];
        int x2 = a[i+1][0];
        int y2 = a[i+1][1];

        int w = dir(x1, y1, x2, y2);
        while(y1 != y2)
        {
            b[y1-ymin-(1-w)/2][(1+w)/2] = x1;
            y1 += w;
        }
    }

    for (int s = -lines - k; s < -lines; ++s)
    {
        cout << "s = " << s << endl;
        for (int i = lines - 1; i >= 0; --i)
        {
            for (int x = 0; x < xmax + 2; ++x)
                cout << "-" << " ";
            cout << endl;
            for (int x = 0; x < xmax + 2; ++x)
            {
                cout << ((x < b[i][1] && x >= b[i][0]) ? "#" : " ");
                cout << (((x - i - s) % k) ? " " : "|");
            }
            cout << endl;
        }
        for (int x = 0; x < xmax + 2; ++x)
            cout << "-" << " ";
        cout << endl;

    }

    int minsum = INT_MAX;
    for (int s = -lines - k; s < -lines; ++s)
    {
        int sum = 0;
        for (int i = 0; i < lines; ++i)
        {
            int l = (b[i][0] - i - s) % k;
            if (l)
                ++sum;
            int r = (k - (b[i][1] - b[i][0] - (k - l)) % k) % k;
            if (r)
                ++sum;
            sum += (b[i][1] - b[i][0] - (k - l) % k - (k - r) % k) / k;
        }
        if (sum < minsum)
            minsum = sum;
    }
    cout << minsum << endl;
}
