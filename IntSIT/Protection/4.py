import os


def main():
    file = 'OUTPUT3.txt'
    os.rename(file, os.path.splitext(file)[0] + '.bak')


if __name__ == "__main__":
    main()
