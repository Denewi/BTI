def main():
    text = sorted(set(list(input('Type string: ').replace(' ', ''))))
    print('Total char:', len(text))
    print(*text)


if __name__ == "__main__":
    main()
