# Лаборатоная №1
Нечетные четырехричные числа, не превышающие 4096 в 10 тичной системе счисления, у которых третья справа цифра равна 2.
Выводит на экран цифры числа, исключая двойки. Вычисляется среднее число между минимальным и максимальным и выводится прописью.
# Лаборатоная №2
Написать программу, решающую задачу из 1 лабораторной работы (в соответствии со своим вариантом) со следующими изменениями:
1.	Входной файл является обыкновенным (т.е. нет требования на «бесконечность» файла);
2.	Распознавание и обработку делать  через регулярные выражения;
3.	В вариантах, где есть параметр (например К), допускается его заменить на любое число;
4.	Все остальные требования соответствуют варианту задания лабораторной работы №1.
# Лабораторная №3
Задание:
С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц B,C,D,E 
заполняется случайным образом целыми числами в интервале [-10,10]. Для тестирования использовать не случайное заполнение,
а целенаправленное.

Вариант 12
Формируется матрица F следующим образом:если в В количество простых чисел в нечетных столбцах в области 2 больше,
чем сумма чисел в четных строках в области 1, то поменять в Е симметрично области 1 и 2 местами, иначе С и Е поменять
местами несимметрично. При этом матрица А не меняется. После чего вычисляется выражение: ((К*A)*А– K*A^T).
Выводятся по мере формирования А, F и все матричные операции последовательно.
# Лабораторная №4
Заадание:
С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц, B,C,D,E
заполняется случайным образом целыми числами в интервале [-10,10]. Для отладки использовать не случайное заполнение,
а целенаправленное.
Для простоты все индексы в подматрицах относительные.
По сформированной матрице F (или ее частям) необходимо вывести не менее 3 разных графиков.
Программа должна использовать функции библиотек numpy  и mathplotlib

Вариант 12
Формируется матрица F следующим образом: скопировать в нее А и если в В количество простых чисел в нечетных столбцах больше,
чем сумма чисел в четных строках, то поменять местами В и Е симметрично, иначе С и Е поменять местами несимметрично.
При этом матрица А не меняется. После чего если определитель матрицы А больше суммы диагональных элементов матрицы F,
то вычисляется выражение: A^-1*A^T – K * F^-1, иначе вычисляется выражение (A^-1 +G-F^-1)*K, где G-нижняя треугольная матрица, полученная из А.
Выводятся по мере формирования А, F и все матричные операции последовательно.
