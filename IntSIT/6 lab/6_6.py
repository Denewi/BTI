def main():
    """Start the main function."""
    print(
        *map(
            lambda x: x[0] ^ x[1],
            zip(
                map(
                    int,
                    input().split()
                ),
                map(
                    int,
                    input().split()
                )
            )
        )
    )


if __name__ == '__main__':
    main()
