program candy_prog;
var
	a, b, c, circle, candy: integer;
	
begin
	readln(a, b, c);
	
	if (a <= c) and (a <= b div 2) then
		circle := a;
	if (c <= a) and (c <= b div 2) then
		circle := c;
	if (b div 2 <= a) and (b div 2 <= c) then
		circle := b div 2;
	
	candy := 4 * circle;
	a := a - circle;
	b := b - 2 * circle;
	c := c - circle;
	
	if a > 0 then
	begin
		candy := candy + 1;
		if b > 0 then
		begin
			candy := candy + 1;
			if c > 0 then
				candy := candy + 1;
		end;
	end;
	
	writeln(candy);
end.
