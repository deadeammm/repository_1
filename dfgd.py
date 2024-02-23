"""
Нечетные четырехричные числа, не превышающие 409610, у которых третья справа цифра равна 2. Выводит на экран цифры числа, исключая двойки.
Вычисляется среднее число между минимальным и максимальным и выводится прописью.
"""
def number_to_words(num):
    units = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "минус"]
    try:
        num = int(num)
        if num < 0:
            return " ".join([units[10]] + [units[int(digit)] for digit in str(abs(num))])
        else:
            return " ".join([units[int(digit)] for digit in str(num)])
    except (ValueError, IndexError):
        return "Неверный ввод. Пожалуйста, укажите действительный номер."


def find_numbers_in_file(file_path):
    numbers = []
    with open(file_path, 'r') as file:
        for line in file:
            for word in line.split():
                try:
                    num = int(word, 4)
                    if num < 4096 and num % 2 != 0:
                        if len(word) >= 3 and word[-3] == '2':
                            numbers.append(num)
                except ValueError:
                    pass
    return numbers


file_path = 'input.txt'
valid_numbers = find_numbers_in_file(file_path)
print(valid_numbers)


def exclude_digit_two(numbers):
    return [int("".join(filter(lambda x: x != '2', str(num)))) for num in numbers]


filtered_numbers = exclude_digit_two(valid_numbers)

# Проверка на наличие чисел в filtered_numbers
if filtered_numbers:
    min_number = min(filtered_numbers)
    max_number = max(filtered_numbers)

    print('Минимальное число:', min_number)
    print('Максимальное число:', max_number)

    if valid_numbers:
        avg_num = sum(valid_numbers) // len(valid_numbers)
        avg_words = number_to_words(avg_num)
        print(f"Среднее число между минимальным и максимальным ({min_number} и {max_number}) прописью: {avg_words}")
    else:
        print("Нет подходящих чисел для нахождения среднего.")
else:
    print("Нет подходящих чисел для нахождения минимального и максимального.")
