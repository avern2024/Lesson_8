def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы - {i}')
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    if not isinstance(numbers, (list, tuple)):
        try:
            numbers = list(numbers)
        except TypeError:
            print(f'В numbers записан некорректный тип данных')
            return None
    result, incorrect_data = personal_sum(numbers)

    try:
        return result / (len(numbers) - incorrect_data) if (len(numbers) - incorrect_data) > 0 else 0
    except ZeroDivisionError:
        return 0


if __name__ == '__main__':
    # Пример выполнения программы:
    print(f'Результат 1: {calculate_average("1, 2, 3")}')
    print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
    print(f'Результат 3: {calculate_average(567)}')
    print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
