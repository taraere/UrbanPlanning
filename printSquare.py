"""
NAME    printSquare

AUTHORS Christiaan Wewer
        Tara Elsen
        jos feenstra        1196 95

DESC    STATE SPACE estimation calculation

NOTE    this thing is an example of how to use helpers
"""

from helpers import *

def main():
    ht = initHouseTypes()

    # what i want to make:
    #

    #test
    #print(h)
    for house in ht:
        print()
        print(house.name)
        printstr = "| ring: {:2}   x: {:2}   y: {:3}   area: {:3}   landValue: {:5} |"
        print((len(printstr) - 4) * "-")
        for r in house.ring:
            print(printstr.format(r.ring, r.x, r.y, round(r.area), round(r.landValue, 1) ))
        print((len(printstr) - 4) * "-")


if __name__ == "__main__":
    main()


# questions about the case:
# can we turn bungalows & maisons ?
# can we
