//Задача 40: Напишите программу, которая принимает на вход три числа и проверяет, может ли существовать треугольник с сторонами такой длины.
// Теорема о неравенстве треугольника: каждая сторона треугольника меньше суммы двух других сторон.

Console.Clear();

Console.WriteLine("Введите сторону a:");
int side_a = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Введите сторону b:");
int side_b = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Введите сторону c:");
int side_c = Convert.ToInt32(Console.ReadLine());

int max = 0;

max = (side_a >= side_b) ? side_a : 0;
max = (max <= side_c) ? side_c : 0;
string output = (max < (side_a + side_b)) ? "Треугольник существует" : "Треугольник не существует";

Console.WriteLine(output);
