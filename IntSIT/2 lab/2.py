"""Leap year."""


def main():
    """Start the main function."""
    while 1:
        n = int(input())
        if (n % 4) == 0 and (n % 100) != 0 or (n % 400) == 0:
            print('YES')
        else:
            print('NO')
        print()


if __name__ == '__main__':
    main()
