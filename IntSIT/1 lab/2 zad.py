"""Сумма цифр 3-х значного числа."""


def main():
    """Главная функция."""
    n = input('Введите 3-х значное число: ')
    sum_n(n)


def sum_n(n):
    """Сложение цифр числа."""
    sum = 0
    for char in n:
        sum += int(char)

    print(sum)


if __name__ == '__main__':
    main()
