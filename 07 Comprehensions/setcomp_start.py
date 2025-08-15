# Demonstrate how to use set comprehensions


def main():
    # define a list of temperature data points
    ctemps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]

    # TODO: build a set of unique Fahrenheit temperatures
    ftemp = {t*(9/5)+32 for t in ctemps}
    print(ftemp)

    # TODO: build a set from an input source
    chars = "The India got 3 Bronch medal in Olympic"
    unique = {c.upper() for c in chars if not c.isspace()}
    print(unique)

if __name__ == "__main__":
    main()
