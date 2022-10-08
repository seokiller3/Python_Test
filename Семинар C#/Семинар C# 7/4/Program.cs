Console.Clear();

Console.WriteLine("Введите количество строк двумерного массива");
int rowCount = int.Parse(Console.ReadLine());

Console.WriteLine("Введите количество столбцов двумерного массива");
int columnCount = int.Parse(Console.ReadLine());

int[,] array = FillArray(rowCount, columnCount, 1, 10);
Console.WriteLine("Сгенерированный массив: ");
PrintArray(array);
Console.WriteLine(" ");
Console.WriteLine("Измененный массив: ");
PrintArray(MakeSq(array));

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
int[,] MakeSq(int[,] array)
{
    int rows = array.GetLength(0);
    int columns = array.GetLength(1);
    for (int i = 0; i < rows; i+=2)
    {
        for (int j = 0; j < columns; j+=2)
        {
            //if (i % 2 == 0 && j % 2 == 0)
                array[i, j] = Convert.ToInt32(Math.Pow(array[i, j], 2));
        }
    }
    return array;
}