"""Show menu."""


def main():
    """Start the main function."""
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    s = merge(a, b)
    print(s)


def merge(a, b):
    """Merge list a amd b."""
    s = []
    el_a = a.pop(0)
    el_b = b.pop(0)
    for i in range(len(a) + len(b) + 2):
        if el_a > el_b:
            s.append(el_b)
            if b:
                el_b = b.pop(0)
            else:
                el_b = float("inf")
        else:
            s.append(el_a)
            if a:
                el_a = a.pop(0)
            else:
                el_a = float("inf")

    return s


if __name__ == '__main__':
    main()
