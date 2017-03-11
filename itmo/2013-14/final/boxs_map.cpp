#include <iostream>
#include <map>
#include <vector>

using namespace std;

int main()
{
    int n;
    cin >> n;
    multimap<int, vector<int> > boxs;
    for (int i = 0; i < n; ++i)
    {
		vector<int> box(4);
		box[0] = i + 1;
        cin >> box[1] >> box[2] >> box[3];
		boxs.insert(make_pair(box[1] + box[2] + box[3], box));
    }
	
	bool fit = true;
	auto it = boxs.begin();
	auto it_prev = it++;
	while (it != boxs.end())
	{
		if (it_prev->second[1] > it->second[1] && (it_prev->second[2] > it->second[2] && it_prev->second[3] > it->second[3]) || (it_prev->second[2] > it->second[3] && it_prev->second[3] > it->second[2]))
			fit = false;
		it_prev = it++;
	}
	
	if (fit)
	{
	    for (auto box: boxs)
			cout << box.second[0] << ' ';
		cout << endl;
	}
	else
		cout << -1 << endl;
	
    return 0;
}
