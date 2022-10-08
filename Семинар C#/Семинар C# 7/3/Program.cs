//Задача 53: Задайте двумерный массив. Напишите программу, которая поменяет местами первую и последнюю строку массива.

Console.Clear();

Console.WriteLine("Введите количество строк двумерного массива");
int rowCount = int.Parse(Console.ReadLine());

Console.WriteLine("Введите количество столбцов двумерного массива");
int columnCount = int.Parse(Console.ReadLine());

int[,] array = FillArray(rowCount, columnCount, 1, 10);
Console.WriteLine("Сгенерированный массив: ");
PrintArray(array);
Console.WriteLine(" ");
Console.WriteLine("Перемещенный массив: ");

int[,] FillArray(int rows, int columns, int min, int max)
{
    int[,] filledArray = new int[rows, columns];

    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            filledArray[i, j] = new Random().Next(min, max + 1);
        }
    }
    return filledArray;
}

void PrintArray(int[,] inputArray)
{
    for (int i = 0; i < inputArray.GetLength(0); i++)
    {
        for (int j = 0; j < inputArray.GetLength(1); j++)
        {
            Console.Write(" " + inputArray[i, j]);
        }
        Console.WriteLine();
    }
}

FillArra(array);
int[,] FillArra(int[,] filladArra)
{

    for (int i = 0; i < filladArra.GetLength(0); i++)
    {
        for (int j = 0; j < filladArra.GetLength(1); j++)
        {
            if (i == 0)
            {
                (filladArra[i, j], filladArra[filladArra.GetLength(1) - 1, j]) = (filladArra[filladArra.GetLength(1) - 1, j], filladArra[i, j]);
            }
        }
    }
    return filladArra;
}
Console.WriteLine();
PrintArray(array);