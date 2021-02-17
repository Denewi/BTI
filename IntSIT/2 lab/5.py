"""Proper ending."""


def main():
    """Start the main function."""
    n = int(input())
    range_ = [0, 5, 6, 7, 8, 9]
    print('На лугу пасется ', end='')
    if 10 < n < 20 or n % 10 in range_:
        print(n, 'коров')
    elif n % 10 == 1:
        print(n, 'корова')
    else:
        print(n, 'коровы')


if __name__ == '__main__':
    main()
