def main():
    """Start the main function."""
    print(
        len(
            set(
                list(
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
