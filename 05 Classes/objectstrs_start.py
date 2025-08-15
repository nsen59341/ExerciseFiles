# customize string representations of objects


class Person():
    def __init__(self):
        self.fname = "Natasha"
        self.lname = "Sen"
        self.age = 28

    # TODO: use __repr__ to create a string useful for debugging
    def __repr__(self):
        return f'I am {self.fname} {self.lname} and my age is {self.age}'

    # TODO: use str for a more human-readable string
    def __str__(self):
        return f'Person ({self.fname} {self.lname} and my age is {self.age})'
    
    def __bytes__(self):
        mystr = f'Person ({self.fname} {self.lname} and my age is {self.age})'
        return mystr.encode('utf-8')

def main():
    # create a new Person object
    cls1 = Person()

    # use different Python functions to convert it to a string
    print(repr(cls1))
    print(str(cls1))
    # print("Formatted: {0}".format(cls1))
    print(bytes(cls1))


if __name__ == "__main__":
    main()
