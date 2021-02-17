"""Angry boxes."""
from numpy import sort


def main():
    """Start the main function."""
    box1 = []
    box2 = []
    for i in range(3):
        edge = int(input())
        box1.append(edge)
    print()
    for i in range(3):
        edge = int(input())
        box2.append(edge)
    print()

    box1 = sort(box1)
    box2 = sort(box2)
    print(box1, box2)

    if all(box1 == box2):
        print('Boxes are equal')
    elif all(box1 <= box2):
        print('The first box is smaller than the second one')
    elif all(box2 <= box1):
        print('The first box is larger than the second one')
    else:
        print('Boxes are incomparable')


if __name__ == '__main__':
    main()
