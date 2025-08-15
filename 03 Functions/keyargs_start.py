# Demonstrate the use of keyword-only arguments


# use keyword-only arguments to help ensure code clarity
def myFunction(arg1, arg2, *, exc=False):
    print(arg1, arg2, exc)


def main():
    # try to call the function without the keyword
    myFunction(1, 2, exc=True)


if __name__ == "__main__":
    main()
