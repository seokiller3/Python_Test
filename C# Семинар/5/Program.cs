//Напишите программу, которая принимает на вход трёхзначное число и на выходе показывает последнюю цифру этого числа. 456 -> 6 782 -> 2 918 -> 8


Console.Clear();

Console.Write("Введите трехзначное число:");

string num = (Console.ReadLine());

Console.WriteLine(num.ToString()[2]);



Console.WriteLine("Введите трехзначное число: ");
int num = Convert.ToInt32(Console.ReadLine());

int num_dec = num - (num/100)*100;
int num_l = num_dec-(num_dec / 10) * 10;

Console.WriteLine(num_l);



