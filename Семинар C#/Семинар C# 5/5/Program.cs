/*Найдите произведение пар чисел в одномерном массиве.
Парой считаем первый и последний элемент, второй и предпоследний и т.д. Результат запишите в новом массиве.
[1 2 3 4 5] -> 5 8 3
[6 7 3 6]-> 36 21 */

Console.Clear();

int[] MultiplyElem(int[] array_local)
{
    int Len = 0;

        if (array_local.Length % 2 == 0)
        {
        Len = array_local.Length / 2;
        }
        else
        {
        Len = array_local.Length / 2 + 1;
        }

    int[] new_array = new int[Len];

        for (int i = 0; i < Len; i++)
        {
        new_array[i] = array_local[i] * array_local[array_local.Length - 1 - i];
        }

        if (array_local.Length % 2 == 1)
        {
        new_array[Len - 1] = array_local[Len - 1];
        }
    return new_array;
}