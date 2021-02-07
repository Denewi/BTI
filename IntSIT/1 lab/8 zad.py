"""Улиточка."""


def main():
    """Главная функция."""
    while 1:
        length = int(input())
        up = int(input())
        down = int(input())

        print(((length - up - 1) // (up - down)) + 2)
        print()


if __name__ == '__main__':
    main()
