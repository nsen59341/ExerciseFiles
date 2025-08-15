# Demonstrate the usage of namdtuple objects

import collections


def main():
    # TODO: create a Point namedtuple
    Point = collections.namedtuple("Point", "x y z")
    p1 = Point(20,40,30)
    p2 = Point(10,35,40)

    print("The 1st position is: ", p1.x, "x", p1.y, "x", p1.z)
    print("The 2nd position is: ", p2.x, "x", p2.y, "x", p2.z)

    # TODO: use _replace to create a new instance
    p2 = p2._replace(y=18)

    print("The 1st position is: ", p1.x, "x", p1.y, "x", p1.z)
    print("The 2nd position is: ", p2.x, "x", p2.y, "x", p2.z)


if __name__ == "__main__":
    main()
