//Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
//A (3,6); B (2,1) -> 5,09
//A (7,-5); B (1,-1) -> 7,21

Console.Clear();

Console.WriteLine("Введите X1:");
int x1 = int.Parse(Console.ReadLine());

Console.WriteLine("Введите Y1:");
int y1 = int.Parse(Console.ReadLine());

Console.WriteLine("Введите X2:");
int x2 = int.Parse(Console.ReadLine());

Console.WriteLine("Введите Y2:");
int y2 = int.Parse(Console.ReadLine());

double len = Math.Sqrt(Math.Pow((x1 - x2), 2) + Math.Pow((y1 - y2), 2));

Console.WriteLine($"Расстояние между точками =, {len}");