#include <iostream>
#include <vector>

using namespace std;

typedef pair<int, int> Field;
typedef vector<Field> Path;

int map_coins[6][6] = {
	{0, 0, 3, 0, 9, 6},
	{0, 6, 0, 2, 0, 0},
	{0, 0, 3, 0, 0, 5},
	{7, 0, 0, 4, 0, 0},
	{3, 0, 4, 0, 1, 0},
	{0, 10, 0, 1, 0, 0}
};

int steps[4][2] = {
	{+1, 0},
	{-1, 0},
	{0, +1},
	{0, -1}
};

Path best_path;
int best_path_coins = 0;

bool check(Field f)
{
	return (f.first >= 0 && f.first <= 5 && f.second >= 0 && f.second <= 5);
}

bool finish(Field f)
{
	return (f.first == 5 && f.second == 5);
}

void calc_route(int coins, int energy, Path route)
{
	if (finish(route.back()) && coins > best_path_coins)
	{
		best_path = route;
		best_path_coins = coins;
	}
	if (energy == 0)
		return;

	for (int* d: steps)
	{
		Path next_route = route;
		Field next_step = make_pair(route.back().first + d[0], route.back().second + d[1]);

		if ((check(next_step)) && find(route.begin(), route.end(), next_step) == route.end())
		{
			next_route.push_back(next_step);
			calc_route(coins + map_coins[next_step.first][next_step.second], energy - 1, next_route);
		}
	}
}

int main()
{
	calc_route(0, 16, Path(1, make_pair(0, 0)));
	cout << best_path_coins << endl;
	for (Field v: best_path)
		cout << v.first << '\t' << v.second << endl;
}
