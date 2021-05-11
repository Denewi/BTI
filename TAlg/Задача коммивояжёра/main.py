MEANING = []


def main():
    # Создаем граф из файла
    graph, list_city = create_graph_and_list_city()
    list_city.remove(1)
    print(graph)

    record_meaning(graph, list_city, 1, 0)
    print(MEANING)
    with open('OUTPUT01.TXT', 'w') as output_file:
        output_file.write(str(min(MEANING)))


def create_graph_and_list_city():
    graph = {}
    list_city = []
    with open('INPUT01.TXT', 'r') as input_file:
        k = int(input_file.readline())

        # Создаем скелет графа
        for top in range(1, k+1):
            graph[top] = {}
            list_city.append(top)

        # Вносим данные графа
        for top in range(1, k+1):
            line = list(map(int, input_file.readline().split()))
            for i, cost in enumerate(line):
                if cost > 0:
                    graph[top][i+1] = cost

    return graph, list_city


def record_meaning(graph, list_city, node, sum):
    if not list_city and node in graph[1]:
        sum += graph[1][node]
        MEANING.append(sum)
    else:
        for neighbour in graph[node]:
            if neighbour in list_city:
                sum += graph[node][neighbour]
                list_city_temp = list_city.copy()
                list_city_temp.remove(neighbour)
                record_meaning(graph, list_city_temp, neighbour, sum)


if __name__ == "__main__":
    main()
