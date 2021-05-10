def main():
    print(
        sum(
            filter(
                lambda x: x > 0,
                map(
                    int,
                    input().split()
                )
            )
        )
    )


if __name__ == "__main__":
    main()
