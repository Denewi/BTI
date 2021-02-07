"""Считаем пирожки."""


def main():
    """Главная функция."""
    a, b, n = int(input()), int(input()), int(input())
    print(a*n+(b*n)//100, b*n % 100)


if __name__ == '__main__':
    main()
