/*Задача 33: Задайте массив. Напишите программу, которая определяет, присутствует ли заданное число в массиве.
4; массив [6, 7, 19, 345, 3] -> нет
3; массив [6, 7, 19, 345, 3] -> да */

Console.Clear();

Console.WriteLine("\nЗамена элементов массива на противоположный знак: \n");

int arr_length = 5;

Console.WriteLine("Введите число:");
int num = Convert.ToInt32(Console.ReadLine());

int[] filledArray = FillArray(arr_length, -10, 10);

Console.WriteLine("\n Массив");
PrintArray(filledArray);
Console.WriteLine(SearchNum(filledArray, num) ? "\n Да" : "\n Нет");

int[] FillArray(int size, int min, int max)
{
    int[] filledArray = new int[size];

    for (int i = 0; i < filledArray.Length; i++)
    {
        filledArray[i] = new Random().Next(min, max + 1);
    }
    return filledArray;
}

void PrintArray(int[] arr)
{
    Console.WriteLine("\n[" + String.Join(",", arr) + "]");
}

bool SearchNum(int[] arr, int search_num)
{
    for (int i = 0; i < arr_length; i++)
    {
        if (arr[i] == num)
        {
            return true;
        }
    }
    return false;
}