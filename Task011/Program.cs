// Напишите программу, которая выводит массив из 8 элементов, 
// заполненный нулями и единицами в случайном порядке.
// [1,0,1,1,0,1,0,0]

void FillArray(int[] collection)
{
    int length = collection.Length;
    for (int i = 0; i < length; i++)
    {
        collection[i] = new Random().Next(0, 2);
    }
}

void PrintArray(int[] col)
{
    int count = col.Length;
    for (int pos = 0; pos < count; pos++)
    {
        Console.Write(col[pos] + " ");
    } 
}

int[] array = new int[8];

FillArray(array);
PrintArray(array);