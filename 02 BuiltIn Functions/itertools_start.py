# advanced iteration functions in the itertools package
import itertools

def testFunction(x):
    return x<40


def main():
    # TODO: cycle iterator can be used to cycle over a collection
    seq1 = ["Joe", "John", "Mike"]
    cycl = itertools.cycle(seq1)
    # for i in range(6):
    #     print(next(cycl))

    # TODO: use count to create a simple counter
    cnt = itertools.count(150,10)
    # print(next(cnt))
    # print(next(cnt))
    # print(next(cnt))

    # TODO: accumulate creates an iterator that accumulates values
    # vals = [10,20,30,40,50,40,30]
    vals = [30,40,50,40,30,20,10]
    # accmlt = itertools.accumulate(vals)
    # print(list(accmlt))
            
    # TODO: use chain to connect sequences together
    # print(list(itertools.chain('123', 'xyz')))
    
    # TODO: dropwhile and takewhile will return values until
    # a certain condition is met that stops them
    x = list(itertools.dropwhile(testFunction, vals))
    y = list(itertools.takewhile(testFunction, vals))
    print(vals)
    print(x)
    print(y)

    
if __name__ == "__main__":
    main()
    