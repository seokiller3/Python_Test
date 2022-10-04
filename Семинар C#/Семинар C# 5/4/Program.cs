/*Задача 35: Задайте одномерный массив из 123 случайных чисел. Найдите количество элементов массива, значения которых лежат в отрезке [10,99].
Пример для массива из 5, а не 123 элементов. В своём решении сделайте для 123
[5, 18, 123, 6, 2] -> 1
[1, 2, 3, 6, 2] -> 0
[10, 11, 12, 13, 14] -> 5 */

Console.Clear();

Console.WriteLine("\nЗамена элементов массива на противоположный знак: \n");

int arr_length = 123;


int[] filledArray = FillArray(arr_length, 1, 123);

Console.WriteLine("\n Массив");
PrintArray(filledArray);
Console.WriteLine(SearchNum(filledArray));

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

int SearchNum(int[] arr)
{
    int count = 0;
    for (int i = 0; i < arr_length; i++)
    {
        if (arr[i] >= 10 && arr[i] <= 99)
        {
            count ++;
        }
    }
    return count;
}

