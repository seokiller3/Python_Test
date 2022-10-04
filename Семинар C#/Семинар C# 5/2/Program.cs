//Задача 32: Напишите программу замена элементов массива: положительные элементы замените на соответствующие отрицательные, и наоборот.
//[-4, -8, 8, 2] -> [4, 8, -8, -2]

Console.Clear();

Console.WriteLine("\nЗамена элементов массива на противоположный знак: \n");

int arr_length = 4;


int[] filledArray = FillArray(arr_length, -10, 10);
Console.WriteLine("\nРазмер массива: \n {0}", arr_length);
Console.WriteLine("\nИсходный массив");
PrintArray(filledArray);
ChangeArr(filledArray);
Console.WriteLine("\nИзмененный массив");
PrintArray(filledArray);

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

void ChangeArr(int[] arr)
{
    for (int i = 0; i < arr.Length; i++)
    {
        arr[i] = -arr[i];
    }
}