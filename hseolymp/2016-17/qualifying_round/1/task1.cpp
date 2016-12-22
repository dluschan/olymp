#include <iostream>

int main() {
  int n, m;
  std::cin >> n >> m;

  int stop = n / m - (n % m ? 0 : 1);
  int time = n + (1 + stop) * stop / 2;

  std::cout << time << std::endl;
  return 0;
}
