//Напишите программу, которая выводит третью цифру заданного числа или сообщает, что третьей цифры нет.
//645 -> 5
//78 -> третьей цифры нет
//32679 -> 6

Console.Clear();

Console.WriteLine("Введите трехзначное число ");

string a = (Console.ReadLine());

if (a.Length == 3)
{
    Console.WriteLine("Третья цифра: " + a.ToString()[2]);
}
else
{
    Console.WriteLine("Нет третьей цифры");
}