// Задача 70: Напишите программу, которая на вход принимает
// два числа и выдаёт первые N чисел, для которых каждое 
// следующее равно сумме двух предыдущих.
// 3 и 4, N = 5 -> 3 4 7 11 18
// 6 и 10, N = 4 -> 6 10 16 26

// int Fibonacci(int num1, int num2, int n)
// {
//     if (n <= 0) return 0;
//     if (n == 1) return num1;
//     if (n == 2) return num2;
//     return (Fibonacci(num1, num2, n-1) + Fibonacci(num1, num2, n-2));
// }

// int a = 6;
// int b = 10;
// int n = 4;
// for (int i = 1; i <= n; i++)
// {
//     Console.Write(Fibonacci(a, b, i) + " ");
// }


// Задача 71: В некотором машинном алфавите имеются 
// четыре буквы «а», «и», «с» и «в». Покажите все слова, 
// состоящие из n букв, которые можно построить из букв 
// этого алфавита.
 
// n = 2 -> аа, ии, сс, вв, аи, иа, ис, си, ас, са, ав,
// ва, ви, ив, св, вс

// условие - если n == 0 >> string.Empty

// string[] Words(string alpha, int length)
// {
//     string[] result;
//     if (length <= 0)
//     {
//         result = new string[1];
//         result[0] = String.Empty;
//         return result;
//     }

//     string[] temp = Words(alpha, length - 1);
   
//     result = new string[temp.Length * alpha.Length];
//     int count = 0;
//     for (int i = 0; i < temp.Length; i++)
//     {
//         for (int j = 0; j < alpha.Length; j++)
//         {
//             result[count] = temp[i] + alpha[j];
//             count ++;
//         }
//     }
//     return result;

// }

// int n = 4;
// string alphabet = "мнрсв";
// string[] word;
// word = Words(alphabet, n);

// for (int i = 0; i < word.Length; i++)
// {
//     Console.Write(i + 1 + " " + word[i] + " ");
// }


// Задача 72: Заданы 2 массива: info и data. 
// В массиве info хранятся двоичные
// представления нескольких чисел (без разделителя). 
// В массиве data хранится информация о количестве бит, 
// которые занимают числа из массива info. 
// Напишите программу, которая составит массив 
// десятичных представлений чисел массива data 
// с учётом информации из массива info.
// входные данные:
// - data = {0, 1, 1, 1, 1, 0, 0, 0, 1 }
// - info = {2, 3, 3, 1 }
// выходные данные:
// - 1, 7, 0, 1

int[] data = { 0, 1, 1, 1, 1, 0, 0, 0, 1 };
int[] info = { 2, 3, 3, 1 };

int[] result = new int[info.Length];

int count = 0;
int mult = 1;
for (int i = 0; i < info.Length; i++)
{
    mult = 0;
    for (int j = count; j < count + info[i]; j++)
    {
        mult += data[j] * (int)Math.Pow(2, info[i] - j + count - 1);
        Console.WriteLine("Степень: " + (info[i] - j + count - 1));
    }
    count += info[i];
    Console.WriteLine(mult);
}