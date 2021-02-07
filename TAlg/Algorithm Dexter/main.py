"""The implementation of the algorithm Dexter.

The graph is represented in the file "Algorithm Dexter.png"

"""


def main():
    """Start the main function."""
    # create graph
    city = create_city()

    # create costs citys
    costs = create_costs()

    # create list not check sity
    list_cities = ['biysk', 'barnaul', 'novosibirck', 'belokurikha',
                   'tomsk', 'krasnoyarsk', 'omsk']

    used_city = list_cities.pop(0)  # Сity that we processing
    while list_cities:
        used_costs = costs[used_city]   # Cost of the current city
        for neighbor in city[used_city]:
            costs_neighbor = costs[neighbor]
            path_to_neighbor = city[used_city][neighbor]

            # If path on current node less then rewrite the neighbor node
            if used_costs + path_to_neighbor < costs_neighbor:
                costs[neighbor] = used_costs + path_to_neighbor

        # Finding the min path to the neighbor
        min_path = min(city[used_city].values())
        # Entry in used_city the city with min path to it
        used_city = find_city(city, used_city, min_path)
        # Deleting city from the uninitiated cities
        list_cities.remove(used_city)

    for city, value in costs.items():
        print(f'{city:13} {value}')


def create_city():
    """Initialize the city graph."""
    city = {}
    city['biysk'] = {}
    city['biysk']['barnaul'] = 9
    city['biysk']['novosibirck'] = 11
    city['biysk']['belokurikha'] = 8
    city['barnaul'] = {}
    city['barnaul']['tomsk'] = 4
    city['belokurikha'] = {}
    city['belokurikha']['novosibirck'] = 2
    city['novosibirck'] = {}
    city['novosibirck']['barnaul'] = 2
    city['novosibirck']['tomsk'] = 5
    city['novosibirck']['omsk'] = 20
    city['tomsk'] = {}
    city['tomsk']['krasnoyarsk'] = 6
    city['krasnoyarsk'] = {}
    city['krasnoyarsk']['omsk'] = 7
    city['omsk'] = {}
    return city


def create_costs():
    """Initialize the city cost table."""
    infinity = float("inf")
    costs = {}
    costs['biysk'] = 0
    costs['barnaul'] = infinity
    costs['novosibirck'] = infinity
    costs['belokurikha'] = infinity
    costs['tomsk'] = infinity
    costs['krasnoyarsk'] = infinity
    costs['omsk'] = infinity
    return costs


def find_city(city, used_city, min_path):
    """Search for a key by value."""
    for key in city[used_city].keys():
        if city[used_city][key] == min_path:
            return key


if __name__ == '__main__':
    main()
