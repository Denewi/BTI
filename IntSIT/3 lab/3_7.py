"""Show menu."""


def main():
    """Start the main function."""
    s = list(map(int, input().split()))
    max = s[0]
    index = int()
    for num, el in enumerate(s):
        if el >= max:
            max = el
            index = num
    print(max, index)


if __name__ == '__main__':
    main()
