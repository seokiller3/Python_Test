//Задача 55: Задайте двумерный массив. Напишите программу, которая заменяет строки на столбцы. В случае, если это невозможно, программа должна вывести сообщение для пользователя.

Console.Clear();
int arrayRangeMin = -10;
int arrayRangeMax = 10;

Console.WriteLine("Создаем новый массив.");
int rows = UserInput("\nВведите количество строк: ");
int columns = UserInput("Введите количество столбцов: ");

int[,] array = new int[rows, columns];

CreateArray(array);
WriteArray(array);

int[,] arrayTrans = new int[columns, rows];


try
{
    for (int i = 0; i < columns; i++)
    {
        for (int j = 0; j < rows; j++)
        {
            arrayTrans[i, j] = array[j, i];
        }
    }
    Console.WriteLine("\n Создаем транспонированый массив: \n");

    WriteArray(arrayTrans);
}

catch
{
    Console.WriteLine("\n Невозможно транспонировать массив \n");
}
int UserInput(string input)
{
    Console.Write(input);
    int output = int.Parse(Console.ReadLine());
    return output;
}

void CreateArray(int[,] array)
{
    Console.WriteLine("\n Массив чисел: \n\t");
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            array[i, j] = new Random().Next(arrayRangeMin, arrayRangeMax);
        }
    }
}

void WriteArray(int[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            Console.Write("{0, 5}", array[i, j]);
        }
        Console.WriteLine();
    }
}