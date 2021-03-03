"""Show menu."""
from numpy import abs


def main():
    """Start the main function."""
    n = int(input())
    s = list(map(int, input().split()))
    k = int(input())
    diff = float("inf")
    sought = s[0]

    for el in s:
        minus = abs(k - el)
        if minus < diff:
            diff = minus
            sought = el
    print(sought)


if __name__ == '__main__':
    main()
