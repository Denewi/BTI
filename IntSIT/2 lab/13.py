"""Min divisor."""


def main():
    """Start the main function."""
    reverse()


def reverse():
    """Reverse range."""
    n = int(input())
    if n == 0:
        return None
    else:
        reverse()
        print(n)


if __name__ == '__main__':
    main()
