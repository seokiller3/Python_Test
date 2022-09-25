/*Напишите программу, которая принимает на вход пятизначное число и проверяет, является ли оно палиндромом.
14212 -> нет
12821 -> да
23432 -> да
*/ 

Console.Clear();

Console.WriteLine("Введите число для проверки на палиндром:");
string s = Console.ReadLine();

if (s.Reverse().SequenceEqual(s)) Console.WriteLine("Палиндром!");
else Console.WriteLine("Не палиндром");
