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
    #for houseType in ht:
        #houseType.printRingInfo()

    # example house object
    hType = ht[1]
    coordinate = (50, 50)
    ringsToAdd = 3
    someHouse = House(hType, coordinate, ringsToAdd)

    # test
    print(someHouse.type.name)
    print(someHouse.coord)

    # example moveto
    someCoord = (23, 10)
    someHouse.moveTo(someCoord)
    print(someHouse.coord)

    # example move
    someVector = (-100, -100)
    someHouse.move(someVector)
    print(someHouse.coord)

if __name__ == "__main__":
    main()


# questions about the case:
# can we turn bungalows & maisons ?
# can we
