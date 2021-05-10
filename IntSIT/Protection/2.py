from math import radians, sin


def main():
    startAng = int(input('From: '))
    stopAng = int(input('To: '))
    step = int(input('Step: '))

    sinTable(startAng, stopAng, step)


def sinTable(startAng, stopAng, step):
    for ang in range(startAng, stopAng + step, step):
        print(ang, sin(radians(ang)))


if __name__ == "__main__":
    main()
