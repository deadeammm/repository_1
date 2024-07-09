# Доп.Задание
Написать программу на Python, которая генерирует координаты (строка, столбец) для элементов в "зигзагообразной" матрице
размером n x n начиная с правого верхнего угла.
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

Вариант 12.
Формируется матрица F следующим образом:если в В количество простых чисел в нечетных столбцах в области 2 больше,
чем сумма чисел в четных строках в области 1, то поменять в Е симметрично области 1 и 2 местами, иначе С и Е поменять
местами несимметрично. При этом матрица А не меняется. После чего вычисляется выражение: ((К*A)*А-K*A^T).
Выводятся по мере формирования А, F и все матричные операции последовательно.
# Лабораторная №4
Заадание:
С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц, B,C,D,E
заполняется случайным образом целыми числами в интервале [-10,10]. Для отладки использовать не случайное заполнение,
а целенаправленное.
Для простоты все индексы в подматрицах относительные.
По сформированной матрице F (или ее частям) необходимо вывести не менее 3 разных графиков.
Программа должна использовать функции библиотек numpy  и mathplotlib

Вариант 12.
Формируется матрица F следующим образом: скопировать в нее А и если в В количество простых чисел в нечетных столбцах больше,
чем сумма чисел в четных строках, то поменять местами В и Е симметрично, иначе С и Е поменять местами несимметрично.
При этом матрица А не меняется. После чего если определитель матрицы А больше суммы диагональных элементов матрицы F,
то вычисляется выражение: A^-1*A^T – K * F^-1, иначе вычисляется выражение (A^-1 +G-F^-1)*K, где G-нижняя треугольная матрица, полученная из А.
Выводятся по мере формирования А, F и все матричные операции последовательно.
# Лабораторная №5
Задана рекуррентная функция. Область определения функции – натуральные числа. Написать программу сравнительного
вычисления данной функции рекурсивно и итерационно (значение, время). Определить (смоделировать) границы применимости
рекурсивного и итерационного подхода. Результаты сравнительного исследования времени вычисления представить в табличной
и графической форме в виде отчета по лабораторной работе. F(n<5)=10; F(n)=(-1)n*(5F(n-1)-7(n-2)+F(n//5)/(2n)!) (при n >12), F(n)=F(n-2)-F(n-1) (при 5<n<=12)
# Лабораторная №6
Есть требования:
1 часть – написать программу в соответствии со своим вариантом задания.
Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу введя по своему усмотрению в условие минимум одно ограничение на характеристики
объектов (которое будет сокращать количество переборов) и целевую функцию для нахождения оптимального решения.

Вариант 12. Задание: Книжный магазин подает рождественские открытки К видов. Покупателю нужно N открыток. Сформировать
все возможные комплекты покупки.
# Лабораторная №7
Требуется для своего варианта второй части л.р. №6 (усложненной программы) разработать реализацию с использованием
графического интерфейса. Допускается использовать любую графическую библиотеку питона.
Рекомендуется использовать внутреннюю библиотеку питона tkinter. В программе должны быть реализованы минимум одно
окно ввода, одно окно вывода (со скроллингом), одно текстовое поле, одна кнопка.

Вариант 12. Задание: Книжный магазин подает рождественские открытки К видов. Покупателю нужно N открыток. Сформировать
все возможные комплекты покупки.
# Лабораторная №8
- Требуется написать объектно-ориентированную программу с графическим интерфейсом в соответствии со своим вариантом.
- В программе должны быть реализованы минимум один класс, три атрибута, четыре метода (функции).
- Ввод данных из файла с контролем правильности ввода.
- Базы данных использовать нельзя.
- При необходимости сохранять информацию в виде файлов, разделяя значения запятыми или пробелами.
Для GUI использовать библиотеку tkinter.

Вариант 12.
Объекты – факультативы
Функции: сегментация полного списка факультативов по студентам
визуализация предыдущей функции в форме круговой диаграммы
сегментация полного списка факультативов по преподавателям
визуализация предыдущей функции в форме круговой диаграммы
