"""."""
from numpy import abs


def main():
    """Start the main function."""
    count_cities = int(input())
    dist_cities = list(map(int, input().split()))

    for i, el in enumerate(dist_cities):
        dist_cities[i] = (el, i + 1)

    count_bunkers = int(input())
    dist_bunkers = list(map(int, input().split()))

    for i, el in enumerate(dist_bunkers):
        dist_bunkers[i] = (el, i + 1)

    dist_cities.sort()
    dist_bunkers.sort()
    distribution = {}
    for city, i in dist_cities:
        if (len(dist_bunkers) > 1):
            if abs(city - dist_bunkers[0][0]) < abs(city - dist_bunkers[1][0]):
                distribution[i] = dist_bunkers[0][1]
            else:
                dist_bunkers.pop(0)
        else:
            distribution[i] = dist_bunkers[0][1]

    print(*distribution.values())

if __name__ == '__main__':
    main()
