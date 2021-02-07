"""Следующее четное."""


def main():
    """Главная функция."""
    n = int(input())
    print(n + (((n % 2) + 1) % 2) + 1)


if __name__ == '__main__':
    main()
