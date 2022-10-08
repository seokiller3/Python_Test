//Задача 45: Напишите программу, которая будет создавать копию заданного массива с помощью поэлементного копирования.

Console.Clear();

Console.WriteLine("Введите размер массива:");
int arr_size = Convert.ToInt32(Console.ReadLine());

int[] arr = new int [arr_size];
int [] arr_copy = new int [arr_size];

Random rnd = new Random();
for (int i = 0; i < arr_size; i++)
{
    arr[i] = rnd.Next();
}

for (int i = 0; i < arr_size; i++)
{
    arr_copy[i] = arr[i];
}
Console.WriteLine("[" + String.Join(",", arr_copy) + "]");