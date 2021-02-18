"""Calculating count max elements in range."""


def main():
    """Start the main function."""
    n = -1
    k = 0
    range_ = []
    while n != 0:
        n = int(input())
        if n:
            range_.append(n)
    max_el = max(range_)
    for el in range_:
        if max_el == el:
            k += 1
    print(k)


if __name__ == '__main__':
    main()
