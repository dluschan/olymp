#include <iostream>

using namespace std;

int main()
{
	int c, p, n;
	// cin >> c >> p >> n;
	c = 129;
	p = 9;
	n = 2000000000;
	int factories = 0;
	int cookie = 0;
	int production = 1;
	int time = 0;
	while (cookie < n)
	{
		int justfinish = (n - cookie + production - 1) / production;
		int nextfactory = (c - cookie + production - 1) / production;
		int hardfinish = (n - (cookie + nextfactory * production - c) + production + p - 1) / (production + p);
		// cout << "justfinish - " << justfinish << "; nextfactory - " << nextfactory << "; hardfinish - " << hardfinish << endl;
		if (nextfactory + hardfinish < justfinish)
		{
			++factories;
			time += nextfactory;
			cookie += nextfactory * production - c;
			production += p;
		}
		else
		{
			time += justfinish;
			cookie += justfinish * production;
		}
	}
	cout << time << endl;
	return 0;
}