//Окружной этап всероссийской олимпиады школьников по информатике Москва, 14 декабря 2014 г.
//Задача 3. Ремонт дороги

#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    int l, n;
    cin >> l >> n;

    int c = 0;
    int s = 0;

    for (int i = 0; i < n; ++i)
    {
        int r;
        cin >> r;

        if(r == 1)
        {
          if(s == 0)
          {
            ++c;
            s = l;
          }
          --s;
        }
        else
          if(s > 0)
            --s;
    }

    cout << c << endl;
    return 0;
}
