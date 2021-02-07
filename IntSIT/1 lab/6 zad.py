"""ЧASSики."""


def main():
    """Главная функция."""
    n = int(input())
    sec = n % 60
    min = n // 60 % 60
    hour = n // 3600
    print(f'{hour}:{min:02}:{sec:02}')


if __name__ == '__main__':
    main()
