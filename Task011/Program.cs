// Напишите программу, которая выводит массив из 8 элементов, 
// заполненный нулями и единицами в случайном порядке.
// [1,0,1,1,0,1,0,0]

void FillArray(int[] collection)
{
    for (int i = 0; i < collection.Length; i++)
    {
        collection[i] = new Random().Next(0, 2);
    }
}

void PrintArray(int[] col)
{
    for (int pos = 0; pos < col.Length; pos++)
    {
        Console.Write(col[pos] + " ");
    } 
}

int[] array = new int[15];

FillArray(array);
PrintArray(array);