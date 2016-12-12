program gen;
var
	m1, m2: array[0..26*26-1] of integer;
	i: integer;
	sum: integer;
	s: string;
begin
	for i := 0 to 26*26 - 1 do
	begin
		m1[i] := 0;
		m2[i] := 0;
	end;
	readln(s);
	for i := 1 to length(s) - 1 do
		inc(m1[26*(ord(s[i]) - ord('A')) + ord(s[i+1]) - ord('A')]);
	readln(s);
	for i := 1 to length(s) - 1 do
		inc(m2[26*(ord(s[i]) - ord('A')) + ord(s[i+1]) - ord('A')]);

	sum := 0;
	for i := 0 to 26*26 - 1 do
		sum := sum + m1[i] * m2[i];
	writeln(sum);
end.
