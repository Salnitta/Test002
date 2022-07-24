// Написать программу, которая из имеющегося массива строк сформирует массив из строк, 
// длина которых меньше либо равно 3 символа. Первоначальный массив можно ввести с клавиатуры 
// либо задать на старте выполнения алгоритма.
// При решении не рекомендуется пользоваться коллекциями, лучше обойтись исключительно массивами.
// Примеры:
// ["hello", "2", "world", ":-)"] -> ["2", ":-)"]
// ["1234", "1567", "-2", "computer science"] -> ["-2"]
// ["Russia", "Denmark", "Kazan"] -> []

void PrintArray(string[] array)
{
    for (int i = 0; i < array.Length; i++)
    {
        Console.Write($"{array[i]} ");
    }
}

// int ElementCount(string[] array, int lgth)
// {
//     int count = 0;
//     for (int i = 0; i < array.Length; i++)
//     {
//         if (array[i].Length <= lgth) count++;
//     }
//     return count;
// }

// string[] OutputArray(string[] array, int lgth, int size)
// {
//     string[] result = new string[size];
//     int k = 0;
//     for (int i = 0; i < array.Length; i++)
//     {
//         if (array[i].Length <= lgth)
//         {
//         result[k] = array[i];
//         k++;
//         }
//     }
//     return result;
// }

// DateTime dt = DateTime.Now;
// // string[] input = { "hello", "2", "world", ":-)" };
// // string[] input = { "1234", "1567", "-2", "computer science" };
// string[] input = { "Russia", "Denmark", "Kazan" };
// int n = 3;

// int count = ElementCount(input, n);
// if (count < 1) Console.WriteLine("Array is emty");
// else 
// {
//     string[] output = OutputArray(input, n, count);
//     PrintArray(output);
// }
// Console.WriteLine((DateTime.Now - dt).TotalMilliseconds);

string[] ReductionToSize(string[] array, int size)
{
    string[] result = new string[size];
    for (int i = 0; i < size; i++)
    {
        result[i] = array[i];
    }
    return result;
}

string[] OutputArray(string[] array, int lgth)
{
    int count = 0;
    string[] temp = new string[array.Length]; 
    for (int i = 0; i < array.Length; i++)
    {
        if (array[i].Length <= lgth) 
        {
            temp[count] = array[i];
            count++;
        }
    }
    if (count < 1) Console.WriteLine("Array is empty");
    return ReductionToSize(temp, count);
}

DateTime dt = DateTime.Now;
// string[] input = { "hello", "2", "world", ":-)" };
// string[] input = { "1234", "1567", "-2", "computer science" };
string[] input = { "Russia", "Denmark", "Kazan" };
int n = 3;
string[] output = OutputArray(input, n);
PrintArray(output);
Console.WriteLine((DateTime.Now - dt).TotalMilliseconds);
