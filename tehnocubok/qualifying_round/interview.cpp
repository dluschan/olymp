#include <iostream>
#include <string>

using namespace std;

int main()
{
	string s;
	s = "ogoogoogo";
	
	int i = 0;
	while (i < s.size() - 2)
	{
	  if (s.substr(i, 3) == "ogo")
    {
	      s.replace(i, 3, "***");
	      i += 3;
	      while (i < s.size() - 1 && s.substr(i, 2) == "go")
	        s.erase(i, 2);
    }
    else
      ++i;
	}
	cout << s << endl;
	return 0;
}
