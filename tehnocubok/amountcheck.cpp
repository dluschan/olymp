#include <cctype>
#include <iostream>
#include <string>

using namespace std;

string itoa(int n)
{

	char *s = new char[17];
	string u;

	if (n < 0)
	{ // turns n positive
		n = (-1 * n);
		u = "-"; // adds '-' on result string
	}

	int i = 0; // s counter

	do
	{
		s[i++] = n % 10 + '0'; // conversion of each digit of n to char
		n -= n % 10;		   // update n value
	}

	while ((n /= 10) > 0);

	for (int j = i - 1; j >= 0; j--)
	{
		u += s[j]; // building our string number
	}

	delete[] s; // free-up the memory!
	return u;
}

int main()
{
	string s;
	s = "chipsy48";
	s += "l";
	int sum = 0;
	int price = 0;
	int digitsafterdot = -1;
	for (int i = 0; i < s.size(); ++i)
	{
		if (s[i] == '.') //точки
		{
			digitsafterdot = 0;
		}
		if (isdigit(s[i])) //цифры
		{
		  if (digitsafterdot >= 0)
  			++digitsafterdot;
			price = price * 10 + (s[i] - '0');
		}
		if (isalpha(s[i])) //буквы
		{
		  cout << "количество цифр после точки" << digitsafterdot << endl;
			int factor = (digitsafterdot == 2) ? 1 : 100;
			sum += price * factor;
			digitsafterdot = -1;
			price = 0;
		}
	}
	cout << "количество копеек - " << sum << endl;

	int cheap = sum % 100;
	sum /= 100;
	string answer = itoa(sum % 1000);
	sum /= 1000;

	while (sum)
	{
		int rest = sum % 1000;
		sum /= 1000;
		answer = itoa(rest) + "." + answer;
	}
	if (cheap)
	{
		answer += ".";
		if (cheap < 10)
			answer += "0";
		answer += itoa(cheap);
	}

	cout << answer << endl;
}
