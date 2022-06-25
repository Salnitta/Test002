// Задача 41: Пользователь вводит с клавиатуры M чисел. 
// Посчитайте, сколько чисел больше 0 ввёл пользователь.
// 0, 7, 8, -2, -2 -> 2
// -1, -7, 567, 89, 223-> 3

Console.WriteLine ("Введите элементы массива через запятую:");
string array = Console.ReadLine();
string[] elements = array.Split(',');
int[] mass = new int[elements.Length];
int count = 0;
for (int i = 0; i < elements.Length; i++)
{
    mass[i] = int.Parse(elements[i]);
    if (mass[i] > 0) count ++;
}
Console.WriteLine ("Количество элементов больше нуля: " + count);

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
