"""."""


def main():
    """Start the main function."""
    list_mem = list(map(int, input().split()))
    memory = list_mem[0]
    people = list_mem[1]
    list_data = []
    for line in range(people):
        list_data.append(int(input()))
    list_data.sort()
    k = 0
    for data in list_data:
        memory -= data
        if memory < 0:
            break
        k += 1
    print(k)


if __name__ == '__main__':
    main()
