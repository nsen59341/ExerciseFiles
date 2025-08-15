# define enumerations using the Enum base class
from enum import Enum, auto

class Fruits(Enum):
    Apple = 4
    Guava = 5
    Orange = 6
    Mango = auto()

def main():
    pass
    # TODO: enums have human-readable values and types
    print(Fruits.Orange)
    print(type(Fruits.Orange))
    print(repr(Fruits.Guava))

    # TODO: enums have name and value properties
    print(Fruits.Apple.name ,':', Fruits.Apple.value)

    # TODO: print the auto-generated value
    print(Fruits.Mango.name ,':', Fruits.Mango.value)

    # TODO: enums are hashable - can be used as keys
    dic = {}
    dic[Fruits.Apple] = "Red fruit with sweet taste"
    print(dic[Fruits.Apple])


if __name__ == "__main__":
    main()
