from itertools import accumulate


def main():
    """Start the main function."""
    print(
        *accumulate(
            map(
                int,
                input().split()
            ),
            lambda x, y: x + y
        )
    )


if __name__ == '__main__':
    main()
