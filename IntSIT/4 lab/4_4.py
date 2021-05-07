"""."""


def main():
    """Start the main function."""
    fin = open('INPUT4_4.txt', 'r', encoding='utf8')
    people = []
    for line in fin:
        str_ = line.split()
        fam = str_[0]
        name = str_[1]
        pts = int(str_[3])
        people.append([fam, name, pts])
    fin.close()

    people = sorted(people)

    for el in people:
        print(*el)


if __name__ == '__main__':
    main()
