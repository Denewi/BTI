"""Min divisor."""
from numpy import sqrt


def main():
    """Start the main function."""
    n = int(input())

    print(MinDivisor(n))


def MinDivisor(n):
    """Min divisor."""
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            return i
        i += 1
    return n


if __name__ == '__main__':
    main()
