"""
NAME    printSquare

AUTHORS Christiaan Wewer
        Tara Elsen
        jos feenstra        1196 95

DESC    STATE SPACE estimation calculation

NOTE    this thing is an example of how to use helpers
"""

from helpers import *

class House:


    def __init__(self, aType, aCoord, ExtraRings):
        self.type = aType
        self.origin = aCoord
        self.rings = ExtraRings
        self.update()

    def update(self):
        self.coord = self.origin

        # calculate additional geometric information, based on

    def move(self, vector):
        # example vector = (6, -1)
        self.origin = tuple(map(sum, zip(self.origin, vector))

        # change other values with this change
        self.update()

    def moveTo(self, newCoord):
        self.origin = newCoord

        # change other values with this change
        self.update()

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
    print(someHouseInstance.type.name)
    print(someHouseInstance.coord)

    # example moveto
    someCoord = (23, 10)
    someHouse.moveto()
    print(someHouse.coord)

    # example move
    somevector = (-100, -100)
    somehouse.move(someVector)
    print(someHouse.coord)

if __name__ == "__main__":
    main()


# questions about the case:
# can we turn bungalows & maisons ?
# can we
