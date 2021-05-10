"""The task refill.

Statement task in file "task.txt"

The graph from 1 task is represented in the file "1 task.png"

"""


LINK_INPUT = 'INPUT/INPUT01.TXT'
LINK_OUTPUT = 'OUTPUT/OUTPUT01.TXT'


def main():
    """Start the main function."""
    # function read files
    city, list_cities, price_gasoline = read_file()
    N = list_cities[-1]
    # create costs cities
    costs = create_costs(city)

    used_city = list_cities.pop(0)  # Сity that we processing
    while (N in list_cities):
        used_costs = costs[used_city]   # Cost of the current city
        for neighbor in city[used_city]:
            costs_neighbor = costs[neighbor]
            path_to_neighbor = price_gasoline[used_city]

            # If path on current node less then rewrite the neighbor node
            if used_costs + path_to_neighbor < costs_neighbor:
                costs[neighbor] = used_costs + path_to_neighbor

        # Entry in used_city the city with min path to it
        used_city = find_used_city(city, used_city, list_cities,
                                   price_gasoline)

        # Deleting city from the uninitiated cities
        if used_city in list_cities:
            list_cities.remove(used_city)
        else:
            write_file(costs, -1)
            break
    else:
        write_file(costs, costs[N])

    for city, value in costs.items():
        print(f'{city:13} {value:2}')


def read_file():
    """Read file and create graph and costs."""
    with open(LINK_INPUT, 'r') as input_file:

        # create graph
        city = create_city(input_file)

        # create price gasoline cities
        price_gasoline = create_price_gasoline(input_file)

        # create path
        city = create_path(input_file, city)

        # create list not check city
        list_cities = [key for key in city.keys()]

        return city, list_cities, price_gasoline


def edit_str(str):
    """Delete spaces and line break."""
    return str.replace('\n', '').split(' ')


def create_city(input_file):
    """Initialize the city graph."""
    quantity_city = int(edit_str(input_file.readline())[0])

    city = {}

    for city_ in range(1, quantity_city + 1):
        city[str(city_)] = []

    return city


def create_price_gasoline(input_file):
    """Initialize the city cost table."""
    costs_cities = edit_str(input_file.readline())

    price_gasoline = {}

    for city, costs_ in enumerate(costs_cities):
        price_gasoline[str(city + 1)] = int(costs_)

    return price_gasoline


def create_path(input_file, city):
    """Initialize the path cities."""
    quantity_path = int(edit_str(input_file.readline())[0])

    for path in range(1, quantity_path + 1):
        city_start, city_end = edit_str(input_file.readline())
        city[city_start].append(city_end)
        city[city_end].append(city_start)

    return city


def create_costs(city):
    """Initialize the city cost table."""
    infinity = float("inf")

    costs = {}

    for key in city.keys():
        costs[key] = infinity

    costs['1'] = 0

    return costs


def find_used_city(city, used_city, list_cities, price_gasoline):
    """Find next used city."""
    min = float("inf")
    index_min = int()

    for neighbor in city[used_city]:
        if (price_gasoline[neighbor] < min) and (neighbor in list_cities):
            min = price_gasoline[neighbor]
            index_min = neighbor
    return index_min


def write_file(costs, val):
    """Write to file."""
    out = open(LINK_OUTPUT, 'w')
    out.write(str(val))
    out.close()


if __name__ == '__main__':
    main()
