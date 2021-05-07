"""The implementation of the algorithm Dexter.

The graph is represented in the file "Algorithm Dexter.png"

"""


def main():
    """Start the main function."""
    node = create_node()

    costs = create_costs()

    list_cities = ['1', '2', '3', '4', '5']

    k = '1'
    c = []
    f = []

    while k != '5':
        for neighbor in node[k]:
            if node[k][neighbor] > 0 and costs[neighbor] == [float("inf")]:
                c.append([node[k][neighbor], neighbor])
        max_c = max(c)
        costs[max_c[1]] = [max_c[0], k]
        k = max_c[1]
        c = []

    f.append(min(costs.values()))
    for i, node_ in enumerate(costs.values()):
        if node_ != [float("inf")] and node_ != [float("inf"), None]:
            print(i + 1, node_)
    print(f)
    print(costs)

    print()


def create_node():
    """Initialize the node graph."""
    node = {}
    node['1'] = {}
    node['1']['2'] = 20
    node['1']['3'] = 30
    node['1']['4'] = 10
    node['2'] = {}
    node['2']['1'] = 0
    node['2']['3'] = 40
    node['2']['5'] = 30
    node['3'] = {}
    node['3']['1'] = 0
    node['3']['2'] = 0
    node['3']['4'] = 10
    node['3']['5'] = 20
    node['4'] = {}
    node['4']['1'] = 0
    node['4']['3'] = 0
    node['4']['5'] = 20
    node['5'] = {}
    node['5']['2'] = 0
    node['5']['3'] = 0
    node['5']['4'] = 0
    return node


def create_costs():
    """Initialize the node cost table."""
    infinity = float("inf")
    none_ = None
    costs = {}
    costs['1'] = [infinity, none_]
    costs['2'] = [infinity]
    costs['3'] = [infinity]
    costs['4'] = [infinity]
    costs['5'] = [infinity]
    return costs


if __name__ == '__main__':
    main()
