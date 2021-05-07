from functools import reduce


def main():
    """Start the main function."""
    print(
        reduce(
            lambda x, y: x**5 * y**5,
            map(
                int,
                input().split()
            )
        )
    )


if __name__ == '__main__':
    main()
