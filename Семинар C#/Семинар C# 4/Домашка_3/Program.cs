/*Напишите программу, которая задаёт массив из N элементов и выводит их на экран.
1, 2, 5, 7, 19 -> [1, 2, 5, 7, 19]
6, 1, 33 -> [6, 1, 33] */

Console.Clear();

 int[] array = new int[20];
Random myRandom = new Random();
 
Console.WriteLine("Вывод с помощью for");
for (int i = 0; i < array.Length; i++)
     {
        array[i] = myRandom.Next(0, 20);
        Console.Write(array[i] + " ");
     }
 
Console.WriteLine("\n\nВывод с помощью foreach");
foreach (var elem in array)
    {
        Console.Write(elem + " ");
    }