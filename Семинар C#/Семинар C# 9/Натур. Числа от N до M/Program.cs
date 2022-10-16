// Задайте значения N и M. Напишите программу, которая выведет все чётные натуральные числа в промежутке от M до N с помощью рекурсии.
// M = 1; N = 5 -> 2, 4
// M = 4; N = 8 -> 4, 6, 8

Console.WriteLine("Введите число M:");
int M = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Введите число N:");
int N = Convert.ToInt32(Console.ReadLine());

int result = 0;

outputRec(result);

void outputRec(int i)
{
    i--;
    if (i >= 0)
    if (result%2==0)
    {
        outputRec(i);
        Console.Write(" " + (i + 1));
    }
}

// for (int i = 0; i <= N; i++)
//     if (i % 2 == 0)
//     {
//         Console.Write(i + " ");
//     }
