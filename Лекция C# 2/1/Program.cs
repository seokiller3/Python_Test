//Напишите программу, которая выводит случайное число из отрезка [10, 99]
// и показывает наибольшую цифру числа.

//78 -> 8
//12-> 2
//85 -> 8

Console.Clear();

int RandomNum = new Random().Next(10, 100); //74

Console.WriteLine($"Число: {RandomNum}");

int a1 = RandomNum / 10; //7
int a2 = RandomNum % 10; //4

int max = a1;

if (a2 > max)
{
    max = a2;
}

Console.WriteLine($"Максимальная цифра: {max}");