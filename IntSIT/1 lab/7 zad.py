"""Разность времен."""


def main():
    """Главная функция."""
    hour = int(input())
    min = int(input())
    sec = int(input())

    time = hour * 3600 + min * 60 + sec

    hour = int(input())
    min = int(input())
    sec = int(input())

    time = hour * 3600 + min * 60 + sec - time

    print(time)


if __name__ == '__main__':
    main()
