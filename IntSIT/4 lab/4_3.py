"""."""


def main():
    """Start the main function."""
    pts = [[], [], []]
    fin = open('INPUT4_3.txt', 'r', encoding='utf8')
    for line in fin:
        str_ = line.split()
        class_ = int(str_[2])
        pts_ = int(str_[3])
        pts[class_ - 9].append(pts_)
    fin.close()

    for pts_ in pts:
        sum_ = sum(pts_) / len(pts_)
        print(sum_)


if __name__ == '__main__':
    main()
