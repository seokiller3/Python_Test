//Напишите программу, которая на вход принимает два числа и проверяет, является ли первое число квадратом второго.
//a = 25, b = 5 -> да
//a = 2, b = 10 -> нет
//a = 9, b = -3 -> да
//a = -3 b = 9 -> нет

Console.Clear();

Console.Write("Введите число:");

int number = int.Parse(Console.ReadLine());

Console.Write("Введите число:");

int sqrt = int.Parse(Console.ReadLine());

if (Math.Pow(number,2) == sqrt)
{
    Console.WriteLine($"Квадрат числа {number} равен {Math.Pow(number,2)}");
}

else
{
    Console.WriteLine($"Квадрат числа {number} равен {Math.Pow(number,2)}");
}