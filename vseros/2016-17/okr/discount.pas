program discount;
var
a: array[1..100000] of integer;
i, j, n: integer;
begin
  readln(n);
  for i := 1 to n do
    readln(a[i]);
  for i := 1 to n do
  begin
    if a[i] <> 0 then
    begin
      j := i + 1;
      while a[j] <> a[i] * 4 div 3 do
        j := j + 1;
      writeln(a[i]);
      a[j] := 0;
    end;
  end;
end.
