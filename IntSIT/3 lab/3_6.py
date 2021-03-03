"""Show menu."""


def main():
    """Start the main function."""
    s = list(map(int, input().split()))
    k = 0
    for el in s:
        if el > 0:
            k += 1
    print(k)


if __name__ == '__main__':
    main()
