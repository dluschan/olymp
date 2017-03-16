#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main()
{
	int n;
	cin >> n;
	const int duration = 5;

	map<int, int> ad;

	while (n--)
	{
		int a, b;
		cin >> a >> b;
		while (b - a >= duration)
			++ad[a++];
	}

	for (auto p: ad)
		cout << p.first << '\t' << p.second << endl;
	
	vector<pair<int, int> > buf(duration, make_pair(0, 0));
	int firstShow = 0; // максимальное количество просмотров рекламы в первый показ, который соответствует второму показу в момент времени secondShowTime
	int firstShowTime = 0; // время наилучшего первого показа рекламы, который соответствует второму показу в момент времени secondShowTime
	int firstShowTimeBest = 0; // время наилучшего первого показа рекламы, которое соответствует максимальному суммарному числу просмотров
	int secondShowTimeBest = 0; // время наилучшего второго показа рекламы, которое соответствует максимальному суммарному числу просмотров
	int secondShowTimePrev = ad.begin()->first; // предыдующее время, в которое мог начаться второй показ рекламы
	int maxSum = 0; // максимальное суммарное число просмотров рекламы
	for (auto p: ad)
	{
		int secondShowTime = p.first; // предполагаемый момент времени запуска рекламы во второй раз
		int secondShow = p.second;	// количество просмотров рекламы, показанной в момент времени secondShowTime

		int extraBonusTime = secondShowTime - secondShowTimePrev - 1; // количество 
		for (int i = 0; i < extraBonusTime && i < duration; ++i)
		{
			if (buf[(secondShowTimePrev + 1 + i) % duration].second > firstShow)
			{
				firstShow = buf[(secondShowTimePrev + 1 + i) % duration].second;
				firstShowTime = secondShowTimePrev + 1 + i;
			}
			buf[(secondShowTimePrev + 1 + i) % duration].second = 0;
		}
		if (buf[secondShowTime % duration].second > firstShow)
		{
			firstShow = buf[secondShowTime % duration].second;
			firstShowTime = secondShowTime;
		}
		buf[secondShowTime % duration].second = secondShow;
		secondShowTimePrev = secondShowTime;
		if (secondShow + firstShow > maxSum)
		{
			maxSum = secondShow + firstShow;
			secondShowTimeBest = secondShowTime;
			firstShowTimeBest = firstShowTime;
		}
	}
	cout << maxSum << ' ' << firstShowTimeBest << ' ' << secondShowTimeBest << endl;
}
