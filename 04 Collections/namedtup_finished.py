# Demonstrate the usage of namdtuple objects

import collections


def main():
    # create a Point namedtuple
    Point = collections.namedtuple("Point", "x y z")

    p1 = Point(10, 20, 45)
    p2 = Point(30, 40, 50)

    print(p1, p2)
    print(p1.x, p1.y)

    # use _replace to create a new instance
    p1 = p1._replace(x=100)
    print(p1)


if __name__ == "__main__":
    main()
