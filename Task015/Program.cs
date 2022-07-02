// Задача 53: Задайте двумерный массив. 
// Напишите программу, которая поменяет 
// местами первую и последнюю строку массива.

void Print (int[,] array)
{
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            // Console.Write(i + " " + j + ", ");
            Console.Write(array[i, j] + " ");
        }
        Console.WriteLine();
    }
}

// int m = 3, n = 4;
// int[,] mass = new int[m,n];

// for (int i = 0; i < mass.GetLength(0); i++)
// {
//     for (int j = 0; j < mass.GetLength(1); j++)
//     {
//         mass[i,j] = new Random().Next(1, 10);
//     }
// }

// Print(mass);
// Console.WriteLine();

// int help = 0;
// for (int i = 0; i < mass.GetLength(1); i++)
// {
//     // Console.Write(mass[0,i]);
//     // Console.Write(mass[mass.GetLength(0) - 1,i]);
//     help = mass[0,i];
//     mass[0,i] = mass[mass.GetLength(0) - 1,i];
//     mass[mass.GetLength(0) - 1,i] = help;
// }
// Print(mass);


// Задача 55: Задайте двумерный массив. 
// Напишите программу, которая заменяет строки на столбцы. 
// В случае, если это невозможно, программа должна 
// вывести сообщение для пользователя.

// int m = 4, n = 4;
// int[,] mass = new int[m,n];

// for (int i = 0; i < mass.GetLength(0); i++)
// {
//     for (int j = 0; j < mass.GetLength(1); j++)
//     {
//         mass[i,j] = new Random().Next(1, 10);
//     }
// }

// Print(mass);
// Console.WriteLine();

// if (mass.GetLength(0) != mass.GetLength(1))
// {
//     Console.WriteLine("Невозможно поменять строки и столбцы местами");
// }

// int help = 0;
// for (int i = 0; i < mass.GetLength(0); i++)
// {
//     for (int j = i + 1; j < mass.GetLength(1); j++)
//     {
//         help = mass[i,j];
//         mass[i,j] = mass[j,i];
//         mass[j,i] = help;
//     }
// }

// // int help = 0;
// // for (int i = 0; i < mass.GetLength(0); i++)
// // {
// //     for (int j = 0; j < i; j++)
// //     {
// //         help = mass[i,j];
// //         mass[i,j] = mass[j,i];
// //         mass[j,i] = help;
// //     }
// // }

// Print(mass);


// Задача 57: Составить частотный словарь элементов 
// двумерного массива. Частотный словарь содержит информацию 
// о том, сколько раз встречается элемент входных данных.

int m = 4, n = 4;
int[,] mass = new int[m,n];

for (int i = 0; i < mass.GetLength(0); i++)
{
    for (int j = 0; j < mass.GetLength(1); j++)
    {
        mass[i,j] = new Random().Next(0, 3);
    }
}

Print(mass);
Console.WriteLine();

int[] array = new int[mass.Length];
int k = 0;
bool finded = false;
for (int i = 0; i < mass.GetLength(0); i++)
{
    for (int j = 0; j < mass.GetLength(1); j++)
    {
        finded = false;
        for (int l = 0; l < k; l++)
        {
        if (array[l] == mass[i,j]) 
        {
            finded = true;
            break;
        }
        }
       if (!finded)
       {
        array[k] = mass[i,j];
        k++;
       }
    }
}

for (int i = 0; i < k; i++)
{
    Console.Write(array[i] + " ");
}
Console.WriteLine();

int count = 0;
int num = 0;
for (int t = 0; t < k; t++)
{
    num = array[t];
    for (int i = 0; i < mass.GetLength(0); i++)
    {
        for (int j = 0; j < mass.GetLength(1); j++)
        {
        if (mass[i,j] == num) count ++;
        }
    }

    Console.WriteLine($"{num} встречается {count} раз");
}

// Задача 59: Задайте двумерный массив из целых чисел. 
// Напишите программу, которая удалит строку и столбец, 
// на пересечении которых расположен наименьший элемент массива.
// Например, задан массив: 
// 1 4 7 2
// 5 9 2 3
// 8 4 2 4
// 5 2 6 7
// Наименьший элемент - 1, на выходе получим следующий массив:
// 9 4 2
// 2 2 6
// 3 4 7

// int m = 4, n = 4;
// int[,] mass = new int[m,n];

// for (int i = 0; i < mass.GetLength(0); i++)
// {
//     for (int j = 0; j < mass.GetLength(1); j++)
//     {
//         mass[i,j] = new Random().Next(1, 10);
//     }
// }

// Print(mass);
// Console.WriteLine();

// int min = mass[0,0];
// int index1 = 0;
// int index2 = 0;
// for (int i = 0; i < mass.GetLength(0); i++)
// {
//     for (int j = 0; j < mass.GetLength(1); j++)
//     {
//         if (mass[i,j] < min) 
//         {
//             min = mass[i,j];
//             index1 = i;
//             index2 = j;
//         }
//     }
// }
// Console.WriteLine(min);

// int[,] array = new int [mass.GetLength(0) - 1, mass.GetLength(1) - 1];
// int k = 0;
// int l = 0;
// for (int i = 0; i < mass.GetLength(0); i++)
// {
//     for (int j = 0; j < mass.GetLength(1); j++)
//     {
//         if (i != index1 && j != index2)
//         {
//             // Console.Write(mass[i,j] + " ");
//             k = i;
//             if (i > index1) k = i - 1;
//             l = j;
//             if (l > index2) l = j - 1;
//             array[k,l] = mass[i,j];
//         }
//     }
// }

// Print(array);



// Альтернативные варианты решения с семинара

/* Задача 53: Задайте двумерный массив. Напишите программу,
которая поменяет местами первую и последнюю строку
массива. */

// void Print(int[,] arr)
// {
//     for (int i = 0; i < arr.GetLength(0); i++)
//     {
//         for (int j = 0; j < arr.GetLength(1); j++)
//         {
//             Console.Write(arr[i, j] + " ");
//         }
//         Console.WriteLine();
//     }
// }

/* int m = 3, n = 4;
int[,] mass = new int[m, n];

for (int i = 0; i < mass.GetLength(0); i++)
{
    for (int j = 0; j < mass.GetLength(1); j++)
    {
        mass[i, j] = new Random().Next(0, 20);
    }
}

Print(mass);
Console.WriteLine();

int tmp = 0;

for (int j = 0; j < mass.GetLength(1); j++)
{
    tmp = mass[0, j];
    mass[0, j] = mass[mass.GetLength(0)-1, j];
    mass[mass.GetLength(0)-1, j] = tmp;
}

Print(mass); */


/* Задача 55: Задайте двумерный массив. Напишите программу,
которая заменяет строки на столбцы. В случае, если это
невозможно, программа должна вывести сообщение для
пользователя. */


/* int m = 4, n = 4;
int[,] mass = new int[m, n];

for (int i = 0; i < mass.GetLength(0); i++)
{
    for (int j = 0; j < mass.GetLength(1); j++)
    {
        mass[i, j] = new Random().Next(0, 20);
    }
}

Print(mass);
Console.WriteLine();
int tmp = 0;

if (mass.GetLength(0) == mass.GetLength(1))
{
    for (int i = 0; i < mass.GetLength(0); i++)
    {
        for (int j = 0; j < i; j++)
        {
            tmp = mass[i, j];
            mass[i, j] = mass[j, i];
            mass[j, i] = tmp;
        }
    }
    Print(mass);
}
else
{
    Console.WriteLine("Таблица не квадратная, нельзя поменять");
} */

/* Задача 57: Составить частотный словарь элементов
двумерного массива. Частотный словарь содержит
информацию о том, сколько раз встречается элемент
входных данных. */

/* Console.WriteLine("Введите размер массива:");
int m = int.Parse(Console.ReadLine());
int n = int.Parse(Console.ReadLine());

int[,] mass = new int[m, n];

for (int i = 0; i < mass.GetLength(0); i++)
{
    for (int j = 0; j < mass.GetLength(1); j++)
    {
        mass[i, j] = new Random().Next(0, 10);
    }
}

Print(mass);
Console.WriteLine();

int[] array = new int[m*n];
bool num = false;
int k = 0;

for (int i = 0; i < mass.GetLength(0); i++)
{
    for (int j = 0; j < mass.GetLength(1); j++)
    {
        num = false;
        for (int r = 0; r < k; r++)
        {
            if(array[])
        }
        
    }
}

int count = 0; */


// void FillArray(int[,] array)
// {
//     for (int i = 0; i < array.GetLength(0); i++)
//     {
//         for (int j = 0; j < array.GetLength(1); j++)
//         {
//             array[i, j] = new Random().Next(1, 10);
//         }
//     }
// }
// void PrintArray(int[,] array)
// {
//     for (int i = 0; i < array.GetLength(0); i++)
//     {
//         for (int j = 0; j < array.GetLength(1); j++)
//         {
//             Console.Write($"{array[i, j]} ");
//         }
//         Console.WriteLine();
//     }
// }
// int m = 6;
// int n = 6;
// int[,] array = new int[m, n];

// FillArray(array);
// PrintArray(array);
// Console.WriteLine();

// int count = 0;
// int[,] dict = new int[m * n, 2];
// int k = 0;

// bool exist = false;

// for (int i = 0; i < array.GetLength(0); i++)
// {
//     for (int j = 0; j < array.GetLength(1); j++)
//     {
//         exist = false;
//         for (int r = 0; r < k; r++)
//         {
//             if (dict[r, 0] == array[i, j])
//             {
//                 dict[r, 1]++;
//                 exist = true;
//                 break;
//             }
//         }
//         if (!exist)
//         {
//             dict[k, 0] = array[i, j];
//             dict[k, 1]++;
//             k++;
//         }
//     }
// }
// Console.WriteLine("Число | Раз  |");
// for (int i = 0; i < k; i++)
// {
//     for (int j = 0; j < dict.GetLength(1); j++)
//     {

//         Console.Write($" {dict[i, j]}    |");
//     }
//     Console.WriteLine();
// }
