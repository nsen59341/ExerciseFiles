# Demonstrate the usage of OrderedDict objects

from collections import OrderedDict


def main():
    # list of sport teams with wins and losses
    sportTeams = [("Royals", (18, 12)), ("Rockets", (24, 6)), 
                ("Cardinals", (20, 10)), ("Dragons", (22, 8)),
                ("Kings", (15, 15)), ("Chargers", (20, 10)), 
                ("Jets", (16, 14)), ("Warriors", (25, 5))]

    # sort the teams by number of wins
    sortedTeams = sorted(sportTeams, key=lambda t: t[1][0], reverse=True)

    # TODO: create an ordered dictionary of the teams
    orderedSportTeams = OrderedDict(sortedTeams)
    # print(orderedSportTeams)

    # TODO: Use popitem to remove the top item
    topPlayer = orderedSportTeams.popitem(False)
    print(topPlayer[0])

    # TODO: What are next the top 4 teams?
    for i,tm in enumerate(orderedSportTeams, start=1):
        print(i, tm)
        if i==4:
            break


    # TODO: test for equality
    d1 = OrderedDict({'a':2, 'b':4})
    d2 = OrderedDict({'b':4, 'a':2})
    print(d1==d2)

if __name__ == "__main__":
    main()
