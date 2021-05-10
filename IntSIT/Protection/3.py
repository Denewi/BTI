def main():
    n = int(input('n: '))

    with open("OUTPUT3.txt", "w") as output_file:
        for i in range(1, n):
            output_file.write(' '.join(str(i*j) for j in range(1, n)) + '\n')


if __name__ == "__main__":
    main()
