def main():
    print(
        input('Filename: ').split('.')[-2].split('\\')[-1] + '.bak'
    )


if __name__ == "__main__":
    main()
