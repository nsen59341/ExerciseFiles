# use iterator functions like enumerate, zip, iter, next


def main():
    # define a list of days in English and French
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

    # TODO: use iter to create an iterator over a collection
    # i = iter(days)
    # print(next(i))
    # print(next(i))
    # print(next(i))

    # TODO: iterate using a function and a sentinel
    # with open("/home/natasha/pythoncodes/Exercise Files/02 BuiltIn Functions/testfile.txt", "r") as fl:
    #     for line in iter(fl.readline,''): # ''-> stop value
    #         print(line)

    # TODO: use regular interation over the days
    
    # TODO: using enumerate reduces code and provides a counter
    # for i in enumerate(days, start=1):
    #     print(i,m)

    # TODO: use zip to combine sequences
    for i,m in enumerate(zip(days, daysFr)):
        print(i, m[0], m[1])


if __name__ == "__main__":
    main()
