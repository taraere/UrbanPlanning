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
    hType = [ht[0], ht[2], ht[0], ht[1], ht[2], ht[0], ht[2], ht[0], ht[1], ht[2]]
    coordinate = [(50, 50), (64, 21), (54, 50), (84, 97), (12, 23), (45, 56), (100, 100), (30, 30), (200, 54)]
    ringsToAdd = [3, 3, 6, 4, 7, 8, 9, 3, 0, 0]

    # # example move
    # someVector = (100, 100)
    # someHouse.move(someVector)
    # print(someHouse.coord)

    houses = []
    for i in range(len(coordinate)):
        houses.append(House(hType[i], coordinate[i], ringsToAdd[i]))

    # draw the board
    drawAll(houses)

if __name__ == "__main__":
    main()


# questions about the case:
# can we turn bungalows & maisons ?
# can we
