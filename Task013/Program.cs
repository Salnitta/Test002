
// Напишите программу, которая перевернёт 
// одномерный массив (последний элемент будет 
// на первом месте, а первый - на последнем и т.д.)
// [1 2 3 4 5] -> [5 4 3 2 1] 
// [6 7 3 6] -> [6 3 7 6]

// void Fill(int[] arr)
// {
//     for (int i = 0; i < arr.Length; i++)
//     {
//         arr[i] = new Random().Next(1, 10);
//     }
// }

// void Print (int[] arr)
// {
//     for (int i = 0; i < arr.Length; i++)
//     {
//         Console.Write(arr[i] + " ");
//     }
//     Console.WriteLine();
// }

// void ArrayFlip (int[] arr)
// {
//     int save;
//     for (int i = 0; i < arr.Length / 2; i++)
//     {
//         save = arr[i];
//         arr[i] = arr[arr.Length - 1 - i];
//         arr[arr.Length - 1 - i] = save;
//     }
// }

// int[] mass = new int[7];
// Fill(mass);
// Print(mass);
// ArrayFlip(mass);
// Print(mass);


// Напишите программу, которавя принимает 
// на вход три числа и проверяет, может ли 
// существовать треугольник со сторонами 
// такой длины

// Console.WriteLine("Введите три числа:");
// int A = int.Parse(Console.ReadLine());
// int B = int.Parse(Console.ReadLine());
// int C = int.Parse(Console.ReadLine());

// if ((A + B) > C && (A + C) > B && (B + C) > A)
// Console.WriteLine("Треугольник");
// else Console.WriteLine("Не треугольник");

// Задача 42: Напишите программу, которая 
// будет преобразовывать десятичное число 
// в двоичное.

// void Print (int[] arr)
// {
//     for (int i = 0; i < arr.Length; i++)
//     {
//         Console.Write(arr[i] + " ");
//     }
//     Console.WriteLine();
// }

// void ArrayFlip (int[] arr)
// {
//     int save;
//     for (int i = 0; i < arr.Length / 2; i++)
//     {
//         save = arr[i];
//         arr[i] = arr[arr.Length - 1 - i];
//         arr[arr.Length - 1 - i] = save;
//     }
// }

// Console.WriteLine("Введите целое положительное число:");
// int dec = int.Parse(Console.ReadLine());
// int save = dec;
// int count = 0;
// while (save > 0)
// {
//     count ++;
//     save = save / 2;
// }

// int[] mass = new int[count];
// for (int i = 0; i < count; i++)
// {
//     mass[i] = dec % 2;
//     dec = dec / 2;
// }

// ArrayFlip(mass);
// Print(mass);

// Альтернативное решение через строку:

// string BinaryConverter(int numb10)
// {
//     string res = string.Empty;
//     for (; numb10 > 0; numb10 = numb10 / 2)
//     {
//         res = numb10 % 2 + res;
//     }
//     return res;
// }
// Console.WriteLine("Введите десятичное число: ");
// int dec = int.Parse(Console.ReadLine());
// Console.WriteLine(BinaryConverter(dec));

// Задача 44: Не используя рекурсию, выведите 
// первые N чисел Фибоначчи. Первые два числа
// Фибоначчи: 0 и 1.
// Если N = 5 -> 0 1 1 2 3 Если N = 3 -> 0 1 1
// Если N = 7 -> 0 1 1 2 3 5 8

// Console.WriteLine("Введите целое положительное число N:");
// int N = int.Parse(Console.ReadLine());
// int N1 = 0;
// int N2 = 1;
// int help;

// Console.WriteLine("Первые N чисел Фибоначчи:");
// for (int i = 0; i < N; i++)
// {
//     Console.WriteLine($"F({i}) = {N1}");
//     help = N1;
//     N1 = N2;
//     N2 = N2 + help;
// }

// Альтернативное решение с помощью массива:

// void Print (int[] arr)
// {
//     for (int i = 0; i < arr.Length; i++)
//     {
//         Console.Write(arr[i] + " ");
//     }
//     Console.WriteLine();
// }

// Console.WriteLine("Введите целое положительное число N:");
// int N = int.Parse(Console.ReadLine());

// int help;
// int[] mass = new int[N];
// mass[0] = 0;
// mass[1] = 1;

// for (int i = 2; i < N; i++)
// {
//     mass[i] = mass[i - 2] + mass[i - 1];
// }

// Console.WriteLine("Первые N чисел Фибоначчи:");
// Print(mass);

// Задача 45: Напишите программу, которая будет создавать 
// копию заданного массива с помощью поэлементного
// копирования.

// void Print (int[] arr)
// {
//     for (int i = 0; i < arr.Length; i++)
//     {
//         Console.Write(arr[i] + " ");
//     }
//     Console.WriteLine();
// }

// void CopyArray (int[] arr, int[] copy)
// {
//     for (int i = 0; i < arr.Length; i++)
//     {
//         copy[i] = arr[i];
//     }
// }

// int[] mass = new int[10];

// for (int i = 0; i < mass.Length; i++)
// {
//     mass[i] = new Random().Next(1, 10);
// }

// Print(mass);
// int[] copyMass = new int[mass.Length];
// CopyArray(mass, copyMass);
// Print(copyMass);

// // Некорректный способ копирования массива 
// // (если изменится элемент первого массива, 
// // то и во втором массиве он изменится)

// int[] mass2 = mass;

// Print(mass2);

// Задача 41: Пользователь вводит с клавиатуры M чисел. 
// Посчитайте, сколько чисел больше 0 ввёл пользователь.
// 0, 7, 8, -2, -2 -> 2
// -1, -7, 567, 89, 223-> 3

// void Print (int[] arr)
// {
//     for (int i = 0; i < arr.Length; i++)
//     {
//         Console.Write(arr[i] + " ");
//     }
//     Console.WriteLine();
// }

// int SearchPositive (int[] arr)
// {
//     int count = 0;
//     for (int i = 0; i < arr.Length; i++)
//     {
//         if (arr[i] > 0) count ++;
//     }
//     return count;
// }

// Console.WriteLine ("Введите размер массива:");
// int M = int.Parse(Console.ReadLine());
// int[] mass = new int[M];

// Console.WriteLine ("Введите элементы массива:");
// for (int i = 0; i < mass.Length; i++)
// {
//     mass[i] = int.Parse(Console.ReadLine());
// }
// Console.WriteLine ("Заданный массив:");
// Print(mass);
// Console.WriteLine ("Количество элементов больше нуля: " + SearchPositive(mass));

// Рекомендации с лекции:
// string s = Console.ReadLine();
// string[] nums = s.Split(',');

// Console.WriteLine(s);

// int[] mass = new int[nums.Length];
// for (int i = 0; i < nums.Length; i++)
// {
//     Console.WriteLine("Подстрока: " + nums[i]);
//     mass[i] = int.Parse(nums[i]);
//     Console.WriteLine("Уже число в квадрате: " + mass[i] * mass[i]);
// }

// Альтернативный способ решения с помощью string:

// Console.WriteLine ("Введите элементы массива через запятую:");
// string array = Console.ReadLine();
// string[] elements = array.Split(',');
// int[] mass = new int[elements.Length];
// int count = 0;
// for (int i = 0; i < elements.Length; i++)
// {
//     mass[i] = int.Parse(elements[i]);
//     if (mass[i] > 0) count ++;
// }
// Console.WriteLine ("Количество элементов больше нуля: " + count);


// Задача 43. Напишите программу, которая найдёт точку пересечения
// двух прямых, заданных уравнениями y = k1 * x + b1, y = k2 * x + b2; 
// значения b1, k1, b2 и k2 задаются пользователем.
// b1 = 2, k1 = 5, b2 = 4, k2 = 9 -> (-0,5; 5,5)

// Console.WriteLine("Введите значения переменных для прямых, заданных уравнениями:");
// Console.WriteLine("y = k1 * x + b1");
// Console.WriteLine("y = k2 * x + b2");

// Console.Write("b1 = ");
// double b1 = double.Parse(Console.ReadLine());
// Console.Write("k1 = ");
// double k1 = double.Parse(Console.ReadLine());
// Console.Write("b2 = ");
// double b2 = double.Parse(Console.ReadLine());
// Console.Write("k2 = ");
// double k2 = double.Parse(Console.ReadLine());

// double x = (b2 - b1) / (k1 - k2);
// double y = k2 * x + b2;

// Console.WriteLine($"Координаты точки пересечения: х = {x}; y = {y}");


