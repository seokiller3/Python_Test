// Задача 31: Задайте массив из 12 элементов, заполненный случайными числами
// из промежутка [-9, 9]. Найдите сумму отрицательных и положительных элементов массива.
//Например, в массиве [3,9,-8,1,0,-7,2,-1,8,-3,-1,6]
// сумма положительных чисел равна 29, сумма отрицательных равна -20.
Console.Clear();

int[] array = FillArray(12, -9, 9);

int positiveSum = 0;
int negativeSum = 0;

Console.WriteLine("[" + String.Join(",",array)+ "]");

foreach(int element in array){
positiveSum += element > 0 ? element : 0; //positiveSum += element -> // positiveSum = element + positiveSum
negativeSum += element < 0 ? element : 0;
}

Console.WriteLine("Положительные числа в массиве:" + positiveSum);
Console.WriteLine("Отрицательные числа в массиве:" + negativeSum);


int[] FillArray(int size, int min, int max)
{
int[] filledArray = new int[size];

for (int i = 0; i < filledArray.Length; i++)
{
filledArray[i] = new Random().Next(min, max + 1);
}
return filledArray;
}