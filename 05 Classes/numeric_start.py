# give objects number-like behavior


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Point x:{0},y:{1}>".format(self.x, self.y)

    # TODO: implement addition
    def __add__(self, other):
        return "<Point x:{0},y:{1}>".format(self.x+other.x, self.y+other.y)

    # TODO: implement subtraction
    def __sub__(self, other):
        # self.x = self.x-other.x
        # self.y = self.y-other.y
        # return self
        return "<Point x:{0},y:{1}>".format(self.x-other.x, self.y-other.y)

    # TODO: implement in-place addition
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __mul__(self, other):
        print(self, other)
        # self.x = self.x-other.x
        # self.y = self.y-other.y
        # return self
        return "<Point x:{0},y:{1}>".format(self.x*other.x, self.y*other.y)


def main():
    # Declare some points
    p1 = Point(10, 20)
    p2 = Point(30, 30)
    print(p1, p2)

    # TODO: Add two points
    p3 = p1+p2 
    print(p3)

    # TODO: subtract two points
    p4 = p2-p1
    print(p4)

    # TODO: Perform in-place addition
    p1 += p2 
    print(p1)

    # TODO: multiply two points
    p5 = p1*p2
    print(p5)

    p6 = p2*p1
    print(p6)


if __name__ == "__main__":
    main()
