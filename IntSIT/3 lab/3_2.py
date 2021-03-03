"""Show menu."""


def main():
    """Start the main function."""
    s = '0123h567h9h0123'
    start = s.find('h')
    finish = s.rfind('h') + 1
    s = s[:start] + s[finish:]
    print(s)


if __name__ == '__main__':
    main()
