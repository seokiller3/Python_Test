// Задача 65: Задайте значения M и N. Напишите программу, которая выведет все натуральные числа в промежутке от M до N с помощью рекурсии
// M = 1; N = 5 -> "1, 2, 3, 4, 5"
// M = 4; N = 8 -> "4, 5, 6, 7, 8"

Console.Clear();

Console.Write("Введите число: ");
int number3 = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите число: ");
int number4 = Convert.ToInt32(Console.ReadLine());
void PrintMN(int number3, int number4)
{
    Console.Write(number3 + ", ");
    number3++;
    if (number3 == number4)
    {
        Console.Write(number4);
        return;
    }
    else
    {
        PrintMN(number3, number4);
    }
}
PrintMN(number3, number4);