string[] CreateArray(int size)
{
    return new string[size];
}

void FillArray(string[] array)
{
   for (int i = 0; i < array.Length; i++)
    {
        Console.WriteLine($"Please, enter string №{i + 1} of the input array:");
        array[i] = Console.ReadLine();
    } 
    Console.WriteLine();
}

int ElementsCounter(string[] array, int length)
{
    int count = 0;
    for (int i = 0; i < array.Length; i++)
    {
        if (array[i].Length <= length) count++;
    }
    return count;
}

string[] MainTask(string[] array, string[] result, int length) 
{
    int count = 0;
    for (int i = 0; i < array.Length; i++)
    {
        if (array[i].Length <= length)
        {
        result[count] = array[i];
        count++;
        }
    }
    return result;
}

string PrintArray(string[] array)
{
    string output = String.Empty;
    for (int i = 0; i < array.Length; i++)
    {
        output += ($"string[{i + 1}]: {array[i]} \n");
    }
    return output;
}

int length = 3;
Random rnd = new Random(); 
int size = rnd.Next(3, 6); // диапазон от 3 до 5 выбран, чтобы генерация с консоли у проверяющего не занимала много времени
string[] inputArray = CreateArray(size);
FillArray(inputArray);

string input = PrintArray(inputArray);
Console.WriteLine("Input array:");
Console.WriteLine(input);

int count = ElementsCounter(inputArray, length);
string[] outputArray = CreateArray(count);
outputArray = MainTask(inputArray, outputArray, length);

string output = PrintArray(outputArray);
Console.WriteLine("Output array:");
Console.WriteLine(output);