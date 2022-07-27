// Задачи с практикума

// 1 коммит - readme файл
// 2 коммит - блок-схема
// 3 коммит - создание проекта
// 4 коммит - уточнение в ридми
// 5 коммит - 1 метод
// 6 коммит - 2 метод
// 7 коммит - решение и т.д.
// 8 коммит - создать гитигнор файл
// можно создать базовый из дотнет командой:
// dotnet new gitignore
// желательно не менее 10 коммитов
// отлично, если сделать пуллреквест с одной ветки на другую
// понимание и уточнение по задаче - например, в каком виде эту задачу сдать?
// декомпозиция задачи
// оформление - отсутствие закомментированного кода или явный комментарий, для чего это


// метод Создания массива
// метод Заполнения массива
// метод подсчета количества нужных строк
// метод Решение основной задачи <-- блок_схема!
// метод Печати массива

// создавать все в отдельных ветках, потом мерджить
// свернуть все методы

// в ридми пишем, что делали, как и почему
// Это контрольная работа Татьяны Сальниковой, блок-схема там лежит, поставьте 5
// option + shift + T - перевод















// Написать программу, которая из имеющегося массива строк сформирует массив из строк, 
// длина которых меньше либо равно 3 символа. Первоначальный массив можно ввести с клавиатуры 
// либо задать на старте выполнения алгоритма.
// При решении не рекомендуется пользоваться коллекциями, лучше обойтись исключительно массивами.
// Примеры:
// ["hello", "2", "world", ":-)"] -> ["2", ":-)"]
// ["1234", "1567", "-2", "computer science"] -> ["-2"]
// ["Russia", "Denmark", "Kazan"] -> []

// void PrintArray(string[] array)
// {
//     for (int i = 0; i < array.Length; i++)
//     {
//         Console.Write($"{array[i]} ");
//     }
// }

// DateTime dt = DateTime.Now;
// // string[] input = { "hello", "2", "world", ":-)" };
// // string[] input = { "1234", "1567", "-2", "computer science" };
// string[] input = { "Russia", "Denmark", "Kazan" };
// Console.WriteLine((DateTime.Now - dt).TotalMilliseconds);

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

string[] MainTask(string[] array, int length, int size) 
{
    string[] result = new string[size];
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
string[] outputArray = MainTask(inputArray, length, count);
string output = PrintArray(outputArray);
Console.WriteLine("Output array:");
Console.WriteLine(output);

// else 
// {
//     string output = PrintArray(outputArray);
//     Console.WriteLine($"output {output}");
//     string[] output = OutputArray(input, length, count);
//     PrintArray(output);
// }




// string[] ReductionToSize(string[] array, int size)
// {
//     string[] result = new string[size];
//     for (int i = 0; i < size; i++)
//     {
//         result[i] = array[i];
//     }
//     return result;
// }

// string[] OutputArray(string[] array, int lgth)
// {
//     int count = 0;
//     string[] temp = new string[array.Length]; 
//     for (int i = 0; i < array.Length; i++)
//     {
//         if (array[i].Length <= lgth) 
//         {
//             temp[count] = array[i];
//             count++;
//         }
//     }
//     return ReductionToSize(temp, count); // сцепка кода, плохо
// }

// DateTime dt = DateTime.Now;
// int size = new Random().Next(3, 6);
// string[] inputArray = new string[size];
// for (int i = 0; i < inputArray.Length; i++)
// {
//     Console.WriteLine($"Введите строку №{i + 1} массива: ");
//     inputArray[i] = Console.ReadLine();
// }
// string[] inputArray = { "hello", "2", "world", ":-)" };
// string[] inputArray = { "1234", "1567", "-2", "computer science" };
// string[] inputArray = { "Russia", "Denmark", "Kazan" };
// int n = 3;
// string[] outputArray = OutputArray(inputArray, n);
// if (outputArray.Length == 0) Console.WriteLine($"В заданном массиве нет строк длиной до {n} символов");
// else
// {
//     Console.WriteLine($"Получен массив из {outputArray.Length} строк длиной до {n} символов:");
//     PrintArray(outputArray);
// }
// Console.WriteLine((DateTime.Now - dt).TotalMilliseconds);

// string output = PrintArray(outputArray);
// Console.WriteLine($"output {output}");
// FileWriteAllText("output.txt", output);


// int GetData(string path)