"""Типа 1 лаба решение задачи с лифтом."""


def main():
    """Главная функция."""
    inp_f = open('input.txt', 'r')
    inp = [line.strip().split() for line in inp_f]
    inp_f.close()

    max_floor = int(inp[0][-1])
    inp.pop(0)

    sum = max = 0
    min = 0
    for move in inp:
        if move[0] == 'u':
            sum += int(move[-1])
            if sum > max:
                max = sum
        elif move[0] == 'd':
            sum -= int(move[-1])
            if sum < min:
                min = sum

    print(max_floor - max + min, '\n')

    for floor in range(1 - min, max_floor - max + 1):
        print(floor, floor + sum)


if __name__ == '__main__':
    main()
