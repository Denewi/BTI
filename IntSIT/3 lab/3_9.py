"""Show menu."""


def main():
    """Start the main function."""
    s = list(map(int, input().split()))
    s1 = str()
    for i in range(0, len(s), 2):
        if i + 1 < len(s):
            s1 += str(s[i+1]) + ' ' + str(s[i]) + ' '
        else:
            s1 += str(s[i])
    print(s1)


if __name__ == '__main__':
    main()
