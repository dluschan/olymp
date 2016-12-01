#include <iostream>

using namespace std;

bool ispoly(int x)
{
    int old = x;
    int y = 0;
    while (x)
    {
        y = y * 10 + x % 10;
        x /= 10;
    }
    return old == y;
}

int main()
{
    int n;
    cin >> n;
    int i = 10;
    int num = 0;
    while (num < n)
    {
        if (ispoly(++i))
        {
            ++num;
            cout << num << "\t" << i << endl;
        }
    }
    return 0;
}
