#include <algorithm>
#include <iostream>

int main() {
  int n, m;
  std::cin >> n >> m;
  ++n;
  
  int *cars = new int[n];

  for (int i = 0; i < n; ++i)
    cars[i] = i;

  for (int i = 0; i < m; ++i)
  {
    int a, b;
    std::cin >> a >> b;

	std::swap(cars[a], cars[b]);
  }

  int *pos = new int[n];
  for (int i = 0; i < n; ++i)
  	pos[cars[i]] = i;

  for (int i = 1; i < n; ++i)
  	std::cout << pos[i] << ' ';
  std::cout << std::endl;

  delete[] cars;
  delete[] pos;
  return 0;
}
