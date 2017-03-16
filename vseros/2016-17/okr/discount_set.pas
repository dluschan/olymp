program discount;
type
	old_price = set of integer;
var
  old: old_price;
  i, j, x, n: integer;
  res: string;
begin
  res := '';
  readln(n);
  for i := 1 to n do
  begin
    readln(x);
    
    if x in old then
      exclude(old, x)
    else
    begin
      res := res + inttostr(x) + ' ';
      include(old, 4 * x div 3);
    end;
  end;
  writeln(res);
end.
