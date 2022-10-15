// Задача 59: Задайте двумерный массив из целых чисел. Напишите программу, которая удалит строку и столбец, на пересечении которых расположен наименьший элемент массива.
// Например, задан массив:
// 1 4 7 2
// 5 9 2 3
// 8 4 2 4
// 5 2 6 7
// Наименьший элемент - 1, на выходе получим
// следующий массив:
// 9 2 3
// 4 2 4
// 2 6 7

(int, int) SearchMin(int[,] array)
{
    int minValue = array[0, 0];
    int minIndexRow = 0;
    int minIndexCol = 0;

    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            if (array[i, j] < minValue)
            {
                minValue = array[i, j];
                minIndexRow = i;
                minIndexCol = j;
            }
        }
    }
    return (minIndexRow, minIndexCol);
}

int[,] TransArray(int[,] array)
{
    int[,] ArrayTr = new int[rows - 1, table - 1];
    int RowCount = 0;
    int ColCount = 0;
    for (int i = 0; i < array.GetLength(0); i++)
    {
        if (i == SearchMin(array).Item1)
        {
            continue;
        }
        for (int j = 0; j < array.GetLength(1); j++)
        {
            if (j == SearchMin(array).Item2)
            {
                continue;
            }
            ArrayTr[RowCount, ColCount] = array[i, j];
            ColCount++;
        }
        RowCount++;
        ColCount = 0;

    }
    return ArrayTr;
}