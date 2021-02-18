"""Solve equation."""
from numpy import sqrt


def main():
    """Start the main function."""
    a = float(input())
    b = float(input())
    c = float(input())

    D = b**2 - 4*a*c

    if D < 0:
        print('No solutions')
    elif D == 1:
        print(-b/2*a)
    else:
        print((-b - sqrt(D)) / 2*a, (-b + sqrt(D)) / 2*a)


if __name__ == '__main__':
    main()
