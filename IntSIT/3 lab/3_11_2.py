"""Show menu."""


def main():
    """Start the main function."""
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    s = merge(a, b)
    print(s)


def merge(a, b):
    """Merge list a amd b."""
    if not a and not b:
        return []
    else:
        if a and b:
            if a[0] < b[0]:
                return [a.pop(0)] + merge(a, b)
            else:
                return [b.pop(0)] + merge(a, b)
        elif a and not b:
            return [a.pop(0)] + merge(a, b)
        elif not a and b:
            return [b.pop(0)] + merge(a, b)


if __name__ == '__main__':
    main()
