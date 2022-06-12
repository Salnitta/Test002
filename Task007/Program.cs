// Напишите программу, которая принимает 
// на вход координаты точки (X и Y), причём 
// X ≠ 0 и Y ≠ 0 и выдаёт номер четверти 
// плоскости, в которой находится эта точка

// Console.WriteLine("Введите Х:");
// int X = int.Parse(Console.ReadLine());

// Console.WriteLine("Введите Y:");
// int Y = int.Parse(Console.ReadLine());

// Console.WriteLine($"Координаты Х:{X}, Y:{Y}");

// if(X > 0 && Y > 0)
// {
//     Console.WriteLine(1);
// }
// else if(X < 0 && Y > 0)
// {
//     Console.WriteLine(2);
// }
// else if(X > 0 && Y < 0)
// {
//     Console.WriteLine(3);
// }
// else if(X < 0 && Y < 0)
// {
//     Console.WriteLine(4);
// }
// else
// {
//     Console.WriteLine("Координаты не принадлежат четверти!");
// }


// Напишите программу, которая по заданному
// номеру четверти показывает диапазон 
// возможных координат точек в этой четверти

// Console.WriteLine("Введите номер четверти от 1 до 4:");
// int a = int.Parse(Console.ReadLine());

// if (a == 1)
// {
//     Console.WriteLine("X в диапазоне от 0 до бесконечности; Y в диапазоне от 0 до бесконечности");
// }
// else if (a == 2)
// {
//     Console.WriteLine("X в диапазоне от 0 до минус бесконечности; Y в диапазоне от 0 до бесконечности");
// }
// else if (a == 3)
// {
//     Console.WriteLine("X в диапазоне от 0 до минус бесконечности; Y в диапазоне от 0 до минус бесконечности");
// }
// else if (a == 4)
// {
//     Console.WriteLine("X в диапазоне от 0 до бесконечности; Y в диапазоне от 0 до минус бесконечности");
// }
// else
// {
//     Console.WriteLine("Нет такой четверти");
// }

// Напишите программу, которая принимает 
// на вход координаты двух точек и находит 
// расстояние между ними в 2D пространстве

Console.WriteLine("Введите координаты Х, Y первой точки:");
double x1 = double.Parse(Console.ReadLine());
double y1 = double.Parse(Console.ReadLine());
Console.WriteLine("Введите координаты Х, Y второй точки:");
double x2 = double.Parse(Console.ReadLine());
double y2 = double.Parse(Console.ReadLine());

double x3 = Math.Pow(x1 - x2,2);
double y3 = Math.Pow(y2 - y1,2);

double result = Math.Sqrt(x3 + y3);
Console.WriteLine("Расстояние между двумя точками равно " + Math.Round(result,2));

// Напишите программу, которая принимает на вход
// число (N) и выдаёт таблицу квадратов чисел от 1 до N

// Console.WriteLine("Введите целое положительное число:");
// int N = int.Parse(Console.ReadLine());
// int i = 1;
// while (i <= N)
// {
//     Console.Write(Math.Pow(i,2) + " ");
//     i++;
// }



