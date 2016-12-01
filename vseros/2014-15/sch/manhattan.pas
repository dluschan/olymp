//Всероссийская олимпиада школьников по информатике, 2014-15 уч. год Первый (школьный) этап, г. Москва Задания для 9-11 классов
//Задача 2. Манхэттен

program Navigator;
var
    dir: char;
    x1, y1, x2, y2: integer;
    i, step: integer;
begin
    readln(x1, y1, x2, y2);

    if x2 > x1 then
        dir := 'E'
    else
        dir := 'W';

    step := abs(x2-x1);

    for i := 1 to step do
        write(dir);

    if y2 > y1 then
        dir := 'N'
    else
        dir := 'S';

    step := abs(y2-y1);

    for i := 1 to step do
        write(dir);

    writeln();
end.
