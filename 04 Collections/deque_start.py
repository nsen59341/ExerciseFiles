# deque objects are like double-ended queues

import collections
import string


def main():
    
    # TODO: initialize a deque with lowercase letters
    d = collections.deque(string.ascii_lowercase)
    print(d)

    # TODO: deques support the len() function
    # print(len(d))

    # TODO: deques can be iterated over
    # for i in d:
        # print(i.upper(), end=' ')

    # TODO: manipulate items from either end
    # d.pop()
    # print(d)
    # d.append('$')
    # print(d)
    # d.popleft()
    # print(d)
    # d.appendleft('@')
    # print(d)

    # TODO: rotate the deque
    d.rotate(2)
    print(d)

    d.reverse()
    print(d)

    d.extend((1,3,))
    print(d)

if __name__ == "__main__":
    main()
