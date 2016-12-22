#include <iostream>
#include <vector>
#include <algorithm>

int main(){
   int n, m;
   std::cin >> n >> m;

   std::vector<int> cars(n);
   for(int i = 0; i < n; ++i)
      cars[i] = i;

   for(int i = 0; i < m; ++i){
     int a, b;
     std::cin >> a >> b;
     std::vector<int>::iterator car_a = std::find(cars.begin(), cars.end(), --a);
     std::vector<int>::iterator car_b = std::find(cars.begin(), cars.end(), --b);

     std::swap(*car_a, *car_b);
   }

   for (int i = 0; i < n; ++i)
     std::cout << cars[i] << " ";
  std::cout << std::endl;
  
   return 0;
}
