#include <iostream>

int main() {
  int n, k, t;
  std::cin >> n >> k >> t;

  int *termcount = new int[n];
  int *termticket = new int[n];

  int terminals = 0;
  for (int i = 0; i < n; ++i) {
    std::cin >> termcount[i];
    terminals += termcount[i];
    termticket[i] = 0;
  }

  int *term = new int[terminals];
  for (int i = 0; i < terminals; ++i)
    term[i] = 0;

  for (int i = 0; i < k; ++i) {
    int time;
    std::cin >> time;
    for (int num = 0; num < terminals; ++num) {
      if (time >= term[num]) {
        term[num] = time + t;
        int type = 0;
        ++num;
        for (; num > 0; ++type)
          num -= termcount[type];
        ++termticket[type-1];
        break;
      }
    }
  }

  for (int type = 0; type < n; ++type)
    std::cout << termticket[type] << ' ';
  std::cout << std::endl;

  delete[] termcount;
  delete[] termticket;
  delete[] term;
  return 0;
}
