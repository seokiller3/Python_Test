// Задайте значения M и N. Напишите программу, которая найдёт наибольший общий делитель (НОД) этих чисел с помощью рекурсии.
// M = 28; N = 7 -> 7

Console.WriteLine("Введите число M");
int M = int.Parse(Console.ReadLine());

Console.WriteLine("Введите число N");
int N = int.Parse(Console.ReadLine());

Console.WriteLine("НОД: " + GetNod(M, N));

int GetNod(int firstNum, int secondNum)
{
    if (secondNum == 0)
        return firstNum;
    else
        return GetNod(secondNum, firstNum % secondNum);
}