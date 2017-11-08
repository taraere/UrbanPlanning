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
    ht = initHouseTypes(20)

    # TEST print ring values
    for houseType in ht:
        houseType.printRingInfo()


    # # what i want to make:
    #                       houseType, houselocation, number of extra rings
    # houseInstance = House(ht[1], (50,50), 3)
    # print(houseInstance.type.name)
    # >>> "Bungalow"

if __name__ == "__main__":
    main()


# questions about the case:
# can we turn bungalows & maisons ?
# can we
