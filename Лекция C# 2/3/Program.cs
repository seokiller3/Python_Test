//Напишите программу, которая будет принимать на вход два числа и выводить, является ли второе число кратным первому. Если число 2 не кратно числу 1, то программа выводит остаток от деления.
//34, 5 -> не кратно, остаток 4
//16, 4 -> кратно

Console.Clear();

string a = (Console.ReadLine());
string b = (Console.ReadLine());

if(int.Parse(a) % int.Parse(b) == 0)
{
    Console.WriteLine("Кратно");
}
else
{
    Console.WriteLine($"Не кратно, остаток = {int.Parse(a) % int.Parse(b)}");
}