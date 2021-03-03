"""Show menu."""


def main():
    """Start the main function."""
    s = list(map(int, input().split()))
    min = s[0]
    max = s[0]
    i_min = int()
    i_max = int()

    for i, el in enumerate(s):
        if el < min:
            min = el
            i_min = i
        if el > max:
            max = el
            i_max = i
    s[i_max], s[i_min] = s[i_min], s[i_max]
    print(*s)


if __name__ == '__main__':
    main()
