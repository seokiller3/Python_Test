//Задача 42: Напишите программу, которая будет преобразовывать десятичное число в двоичное.
//45 -> 101101
//3 -> 11 
//2 -> 10

Console.Clear();

/*Console.WriteLine("Введите число:");
int num = Convert.ToInt32(Console.ReadLine());

Console.WriteLine($"Число {num} в двоичном виде: " + Convert.ToString(num, toBase: 2) + "\n\n");*/

Console.WriteLine("Введите число:");
int num = Convert.ToInt32(Console.ReadLine());

string str = string.Empty;

while (num > 0)
{
    str = num % 2 + str;
    num /= 2;
}
Console.WriteLine(str);