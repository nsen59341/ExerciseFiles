# Demonstrate the use of variable argument lists


# TODO: define a function that takes variable arguments
def addition(base1, base2, *args):
    result = 0
    for arg in args:
        print(arg)
    print("---------")


def main():
    # TODO: pass different arguments
    print(addition(50,60,80))
    lst = [10,20,14,17,22]
    print(addition(*lst))

    # TODO: pass an existing list


if __name__ == "__main__":
    main()
