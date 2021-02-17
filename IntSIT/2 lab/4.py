"""Count even elements in range."""


def main():
    """Start the main function."""
    n = -1
    k = -1
    while n != 0:
        n = int(input())
        if n % 2 == 0:
            k += 1
    print(k)


if __name__ == '__main__':
    main()
