# Demonstrate the use of function docstrings

def myFunction(arg1, arg2):
    """ 
    myFunction -> actually do nothing
    take 2 arguments:  arg1, arg2
    """
    print(arg1, arg2)


def main():
    print(myFunction.__doc__)
    # Output: 
    # myFunction -> actually do nothing
    # take 2 arguments:  arg1, arg2

if __name__ == "__main__":
    main()


#Describe built-in function sorted
print(sorted.__doc__)

# Output:
# Return a new list containing all items from the iterable in ascending order.

# A custom key function can be supplied to customize the sort order, and the
# reverse flag can be set to request the result in descending order.