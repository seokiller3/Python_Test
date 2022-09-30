/*Напишите программу, которая принимает на вход число (А) и выдаёт сумму чисел от 1 до А.
7 -> 28
4 -> 10
8 -> 36
*/

Console.Clear();

Console.WriteLine("Введите число");

int limit = int.Parse(Console.ReadLine());

int GetSumToLimit(int limit)
{
    int result = 0;
    for(int i = 0; i <= limit; i++)  
    {
        result += i;
    }
    return result;
}
Console.WriteLine($"Результат суммы от 1 до {limit} = {GetSumToLimit(limit)}");