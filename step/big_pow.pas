var
	j, i, n, overflow, digits: integer;
	a: array[0..10000] of integer;
begin
	readln(n);
	for i := 0 to n do
		a[i] := 0;

	a[n] := 1;
	digits := 1;
	overflow := 0;
	
	for i := 1 to n do
	begin
		for j := n downto n - digits do
		begin
			a[j] := 2 * a[j] + overflow;
			overflow := a[j] div 10;
			a[j] := a[j] mod 10;
			if (overflow > 0) and (j = n - digits + 1) then
				digits := digits + 1;
		end;
	end;
	for i := n - digits + 1 to n do
		write(a[i]);
	writeln();
end.
