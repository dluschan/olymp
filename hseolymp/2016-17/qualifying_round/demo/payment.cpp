#include <iostream>
#include <set>
#include <functional>

using namespace std;

int main()
{
  int n, k;
  cin >> n >> k;
  set<int, greater<int> > tmin;
  set<int> tmax;
  
  int count = 0;
  for (int i = 0; i < n; ++i)
  {
    int t;
    cin >> t;
    tmax.insert(t);
    tmin.insert(t);
    ++count;

    if (count > k + 1)
    {
      tmax.erase(tmax.begin());
      tmin.erase(tmin.begin());
      --count;
    }
  }
  while (k)
  {
    int tmin0 = *(--tmin.end());
    int tmin1 = *(----tmin.end());
    int tmax0 = *(tmax.begin());
    int tmax1 = *(++tmax.begin());
    if (tmax0 - tmin1 < tmax1 - tmin0) //remove tmin0
      tmin.erase(--tmin.end());
    else
      tmax.erase(tmin.begin());
    --k;
  }
  cout << (*tmax.begin() - *(--tmin.end())) << endl;
  return 0;
}
