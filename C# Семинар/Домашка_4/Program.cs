//Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.

//5 -> 2, 4
//8 -> 2, 4, 6, 8

Console.Clear

Console.Write("Write number: ");

int n = int.Parse(Console.ReadLine());

int i = 1;

while (i <= n);
{
    if (i % 2 == 0)
{
    Console.WriteLine(i);
}

i++;

} 

