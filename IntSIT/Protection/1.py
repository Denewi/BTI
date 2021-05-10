from numpy import sqrt


def main():
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))

    D = b**2 - 4*a*c

    if D > 0:
        print((-b + sqrt(D)) / (2*a))
        print((-b - sqrt(D)) / (2*a))
    elif D == 0:
        print(-b/(2*a))
    else:
        print('No solution')


if __name__ == "__main__":
    main()
