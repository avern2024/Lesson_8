def add_everything_up(a: int | float | str, b: int | float | str):
    try:
        sum_ = a + b
    except TypeError:
        return f'{a}{b}'
    else:
        if isinstance(sum_, float):
            return round(sum_, 3)
        return sum_


if __name__ == '__main__':
    print(add_everything_up(123.456, 'строка'))
    print(add_everything_up('яблоко', 4215))
    print(add_everything_up(123.456, 7))
