def main():
    """Start the main function."""
    print(
        min(
            list(
                filter(
                    lambda x: x % 2,
                    map(
                        int,
                        input().split()
                    )
                )
            )
        )
    )


if __name__ == '__main__':
    main()
