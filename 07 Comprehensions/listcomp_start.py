# Demonstrate how to use list comprehensions


def main():
    # define two lists of numbers
    evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    # TODO: Perform a mapping and filter function on a list
    # new_even = list(map(lambda x: x**2, filter(lambda x: x>4 and x<16, evens)))
    # print(new_even)
    new_even = [x**2 for x in evens]
    print(new_even)

    # TODO: Derive a new list of numbers frm a given list

    # TODO: Limit the items operated on with a predicate condition
    new_odds = [x**2 for x in odds if x>4 and x<16]
    print(new_odds)

if __name__ == "__main__":
    main()
