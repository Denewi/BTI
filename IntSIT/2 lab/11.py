"""Min divisor."""


def main():
    """Start the main function."""
    a = int(input())
    n = int(input())

    print(power(a, n))


def power(a, n):
    """Power a in n."""
    if n == 0:
        return 1
    return a * power(a, n - 1)


if __name__ == '__main__':
    main()
