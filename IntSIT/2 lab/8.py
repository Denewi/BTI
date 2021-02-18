"""Solve equation."""


def main():
    """Start the main function."""
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    f = int(input())

    y = (f*a - c*e) / (a*d - c*b)
    x = (e - b*y) / a

    print(x, y)


if __name__ == '__main__':
    main()
