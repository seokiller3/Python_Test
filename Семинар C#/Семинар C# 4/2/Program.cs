/*Решение в группах задач:
Задача 26: Напишите программу, которая принимает на вход число и выдаёт количество цифр в числе.
456 -> 3
78 -> 2
89126 -> 5 */

Console.Clear();

Console.WriteLine("Введите число:");

int a = (int.Parse(Console.ReadLine()));

Console.WriteLine("Количество цифр = " + a.ToString().Length);