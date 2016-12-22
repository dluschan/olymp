#include <iostream>
#include <queue>
#include <stack>
#include <string>

using namespace std;

class Comp
{
	struct Value
	{
		Value() : t(CHAR) {}
		Value(char c) : t(CHAR), ch(c){};
		Value(int k) : num(k){};
		friend ostream &operator<<(ostream &s, const Value &v) { return ((v.t == CHAR) ? s << v.ch : s << v.num); }

		enum type
		{
			CHAR = 0,
			INT = 1
		};

		type t;
		char ch;
		int num;
	};

  public:
	int operator()(char command)
	{
		switch (command)
		{
		case 'H':
		case 'E':
		case 'L':
		case 'O':
		case 'W':
		case 'R':
		case 'D':
			reg = Value(command);
			break;
		case '@':
			reg = Value(' ');
			break;
		case ']':
			cout << "нужно обработать эту команду тоже";
			break;
		case '.':
			cout << reg;
			break;
		}
		return 0;
	}

  private:
	stack<Value> st;
	queue<Value> q;
	Value reg;
};

int main()
{
	string prog;
	prog = "H.E.L.L.O.@.W.O.R.L.D.'";
	string tap;
	tap = "";
	Comp comp;

	for (size_t i = 0; i < prog.size(); ++i)
		comp(prog[i]);
}
