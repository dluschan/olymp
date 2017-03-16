#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	int qmax;
	float r;
	cin >> r >> qmax;
	float dist = -1.0;
	int p = 0;
	int q = 1;
	int pc, qc;
	while (static_cast<float>(p)/q != r)
	{
		if (static_cast<float>(p)/q > r)
			++q;
		else
			++p;
		if (q > qmax)
			break;
		if (abs(static_cast<float>(p)/q - r) < dist or dist == -1.0)
		{
			pc = p;
			qc = q;
			dist = abs(static_cast<float>(p)/q - r);
		}
	}
	cout << pc << '/' << qc << endl;
}
