"""Sum squares."""


def main():
    """Start the main function."""
    n = int(input())
    print(sum_sqrt(n))


def sum_sqrt(n):
    """Sum sqrt."""
    if n == 1:
        return 1
    return n**2 + sum_sqrt(n - 1)


if __name__ == '__main__':
    main()
