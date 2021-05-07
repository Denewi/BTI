def main():
    """Start the main function."""
    print(
        not all(
            map(
                int,
                map(
                    lambda x: int(input()),
                    range(int(input()))
                )
            )
        )
    )


if __name__ == '__main__':
    main()
