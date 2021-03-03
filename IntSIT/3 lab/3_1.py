"""Show menu."""


def main():
    """Start the main function."""
    s = input()
    print(s[2])     # third symbol
    print(s[-2])    # pre last symbol
    print(s[0:5])   # first five symbols
    print(s[0:-2])  # string without last two symbols
    print(s[::2])   # even symbols
    print(s[1::2])  # even symbols (start 2)
    print(s[::-1])  # reverse
    print(s[::-2])  # reverse odd symbols
    print(len(s))   # string lenght


if __name__ == '__main__':
    main()
