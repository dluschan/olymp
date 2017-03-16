#include <iostream>
#include <fstream>

using namespace std;

const int _MAX_SIZE_ = 1500;
int R[_MAX_SIZE_][_MAX_SIZE_];
int K[_MAX_SIZE_][_MAX_SIZE_];
int a, b, n, q;
int x1, y1, x2, y2;

void remove_linked(int i, int j);

void check(int x_link, int y_link, int x_vertex, int y_vertex)
{
	if ((x_link >= 2*x1 - 2) && (x_link <= 2*x2 - 2) && (y_link >= 2*b - 2*y2) && (y_link <= 2*b - 2*y1) && (K[x_link][y_link] == 1))
	{
		K[x_link][y_link] = 0;

		if ((x_vertex >= 2*x1 - 2) && (x_vertex <= 2*x2 - 2) && (y_vertex >= 2*b - 2*y2) && (y_vertex <= 2*b - 2*y1) && (K[x_vertex][y_vertex] == 1))
			remove_linked(x_vertex, y_vertex);
	}
}

void remove_linked(int i, int j)
{
	check(i - 1, j, i - 2, j);
	check(i + 1, j, i + 2, j);
	check(i, j - 1, i, j - 2);
	check(i, j + 1, i, j + 2);
	K[i][j] = 0;
}

int main()
{
	ifstream fin("input.txt");
	fin >> a >> b >> n >> q;

	for (int i = 0; i < 2*a - 1; ++i)
		for (int j = 0; j < 2*b - 1; ++j)
			R[i][j] = 0;

	for (int stitch = 1; stitch < n; ++stitch)
	{
		char t;
		int x, y;
		fin >> t >> x >> y;
		int xt = 2*x - 2;
		int yt = 2*b - 2*y;

		if (t == 'h')
		{
			R[xt][yt] = 1;
			R[xt+2][yt] = 1;
			R[xt+1][yt] = 1;
		}
		else
		{
			R[xt][yt] = 1;
			R[xt][yt-2] = 1;
			R[xt][yt-1] = 1;
		}
	}

	for (int rec = 0; rec < q; ++rec)
	{
		int polygons = 0;
		fin >> x1 >> y1 >> x2 >> y2;
		int x1t = 2*x1 - 2;
		int y1t = 2*b - 2*y1;
		int x2t = 2*x2 - 2;
		int y2t = 2*b - 2*y2;

		for (int y = y1t; y >= y2t; --y)
			for (int x = x1t; x <= x2t; ++x)
				K[x][y] = R[x][y];

		for (int y = y1t; y >= y2t; ----y)
			for (int x = x1t; x <= x2t; ++++x)
				if (K[x][y] == 1)
				{
					++polygons;
					remove_linked(x, y);
				}

		cout << polygons << endl;
	}

	fin.close();
	return 0;
}
