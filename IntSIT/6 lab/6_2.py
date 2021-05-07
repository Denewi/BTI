def main():
    """Start the main function."""
    print(
        len(
            set(
                list(
                    open('INPUT6_2.txt', 'r', encoding='utf8').read().split()
                )
            )
        )
    )


if __name__ == '__main__':
    main()
