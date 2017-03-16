//Окружной этап всероссийской олимпиады школьников по информатике Москва, 14 декабря 2014 г.
//Задача 2. Заработная плата

#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    int a, b, c, n;
    cin >> a >> b >> c >> n;

    int m = max(a + a % 2, max(2*b, 2*c));
    int lack = (m - a) + (m/2 - b) + (m/2 - c);

    if (n < lack)
    {
      cout << 0 << endl;
      return 0;
    }

    int k = (n - lack) / 4;
    cout << m - a + 2 * k << endl;
    cout << m/2 - b + k << endl;
    cout << m/2 - c + k << endl;

    return 0;
}
