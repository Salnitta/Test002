// Вид 1
// void Method1()
// {
//     Console.WriteLine("Автор ...");
// }
// Method1();

// Вид2
// void Method2(string msg)
// {
//     Console.WriteLine(msg);
// }
// Method2(msg: "Текст сообщения");

// void Method21(string msg, int count)
// {
//     int i = 0;
//     while (i < count)
//     {
//         Console.WriteLine(msg);
//         i++;
//     }
// }
// // Method21("Текст", 4);
// Method21(count: 4, msg: "Новый текст");

// Вид 3

// int Method3()
// {
//     return DateTime.Now.Year;
// }
// int year = Method3();
// Console.WriteLine(year);

// Вид 4

// string Method4(int count, string text)
// {
//     int i = 0;
//     string result = String.Empty;
//     while (i < count)
//     {
//         result = result + text;
//         i++;
//     }
//     return result;
// }

// // Вариант с циклом for

// string Method4(int count, string text)
// {
//     string result = String.Empty;
//     for (int i = 0; i < count; i++)
//     {
//         result = result + text;
//     }
//     return result;
// }

// string res = Method4(10, "z");
// Console.WriteLine(res);

// Задача вывода таблицы умножения на экран

// for (int i = 2; i <= 10; i++)
// {
//     for (int j = 2; j <= 10; j++)
//     {
//         Console.WriteLine($"{i} * {j} = {i * j}");
//     }
//     Console.WriteLine();
// }


// Работа с текстом
// Дан текст. В тексте нужно все пробелы заменить 
// черточками, маленькие буквы "к" заменить
// большими "К", а большие "С" заменить маленькими 
// "с".

// string text = "- Я думаю, - сказал князь, улыбаясь, "
//             + "что, ежели бы вас послали вместо нашего "
//             + "милого Винцегороде, вы бы взяли приступом "
//             + "согласие прусского короля. Вы так "
//             + "красноречивы. Вы дадите мне чаю?";

// // string s = "qwerty"
// //             012
// // s[3] // r

// string Replase(string text, char oldValue, char newValue)
// {
//     string result = String.Empty;
//     int length = text.Length;
//     for(int i = 0; i < length; i++)
//     {
//         if (text[i] == oldValue) result = result + $"{newValue}";
//         else result = result + $"{text[i]}";
//     }
//     return result;
// }

// string newText = Replase(text, ' ', '|');
// Console.WriteLine(newText);
// Console.WriteLine();
// newText = Replase(newText, 'к', 'К');
// Console.WriteLine(newText);
// Console.WriteLine();
// newText = Replase(newText, 'с', 'С');
// Console.WriteLine(newText);
// Console.WriteLine();


// // Задача на сортировку массива методом выбора от минимального к максимальному

// int[] arr = { 1, 2, 3, 9, 4, 5, 5, 6, 7, 1, 1, 8 };

// void PrintArray(int[] array)
// {
//     int count = array.Length;

//     for (int i = 0; i < count; i++)
//     {
//         Console.Write($"{array[i]} ");
//     }
//     Console.WriteLine();
// }

// void SelectionSort(int[] array)
// {
//     for (int i = 0; i < array.Length - 1; i++)
//     {
//         int minPos = i;
        
//         for (int j = i + 1; j < array.Length; j++)
//         {
//             if (array[j] < array[minPos]) minPos = j;
//         }

//         int temp = array[i];
//         array[i] = array[minPos];
//         array[minPos] = temp;
//     }
// }

// PrintArray(arr);
// SelectionSort(arr);
// PrintArray(arr);

// Задача на сортировку массива методом выбора от максимального к минимальному

int[] arr = { 1, 2, 3, 9, 4, 5, 5, 6, 7, 1, 1, 8 };

void PrintArray(int[] array)
{
    int count = array.Length;

    for (int i = 0; i < count; i++)
    {
        Console.Write($"{array[i]} ");
    }
    Console.WriteLine();
}

void SelectionSort(int[] array)
{
    for (int i = 0; i < array.Length - 1; i++)
    {
        int maxPos = i;
        
        for (int j = i + 1; j < array.Length; j++)
        {
            if (array[j] > array[maxPos]) maxPos = j;
        }

        int temp = array[i];
        array[i] = array[maxPos];
        array[maxPos] = temp;
    }
}

PrintArray(arr);
SelectionSort(arr);
PrintArray(arr);



