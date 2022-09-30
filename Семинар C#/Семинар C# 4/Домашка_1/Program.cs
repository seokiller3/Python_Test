/*Напишите цикл, который принимает на вход два числа (A и B) и возводит число A в натуральную степень B.
3, 5 -> 243 (3⁵)
2, 4 -> 16
*/

Console.Clear();

Console.WriteLine("Введите число: ");
int A = int.Parse(Console.ReadLine());

Console.WriteLine("Введите степень, в которую хотите возвести число: ");
int B = int.Parse(Console.ReadLine());

Console.WriteLine(Math.Pow(A, B));