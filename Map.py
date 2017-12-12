import pandas

from House import *
from Rectangle import *

"""
Map class which holds houses and has a method of printing them

METHODS AND THEIR USE:
self.addHouse(type, coord, rings)
self.plot()
"""
class Map:

    def __init__(self, coord1=(0,0), coord2=AREA):
        # init base values
        self.coord1 = coord1
        self.coord2 = coord2
        self.width  = coord2[0] - coord1[0]
        self.height = coord2[1] - coord1[1]

        # init lists to fill with objects
        self.houses = []
        houseIndex = 0
        self.waterBody = []

        # init a boundary for collision testing
        self.boundary = Rectangle(self.coord1, self.width, self.height)



    """
    add a [aType] house to the map at [aCoord], with [addrings] rings
    """
    def addHouseStupid(self, aType, aCoord, addRings):

        # simple way of creating a house
        self.houses.append(House(aType, aCoord, addRings))

    """
    add a [aType] house to the map at [aCoord], with [addrings] rings
    the following options are usable:
        ["non_colliding"]
            pick random house locations until the position is valid.
        ["random_positions"]
            place house at a random starting location
        ["Tactical_fit"]
            TODO
    """
    def addHouse(self, aType, aCoord, addRings, *options):

        # index
        # TODO add index to houses
        # apply options
        LoopUntilValid = False
        if any(option == "non_colliding" for option in options):
            # print()
            print("\n make a house without colliding")
            LoopUntilValid = True
        if any(option == "random_positions" for option in options):
            print("make house at a random location")
            h = (House(aType, "random", addRings))
        else:
            print("make a house in ordinary fashion")
            h = (House(aType, aCoord, addRings))

        # directly append h if we don't need to check for valid position
        if not LoopUntilValid:
            self.houses.append(h)
        else:
            # if we do need to check if placement is valid
            relocateCounter = 0
            MAX_ITERATIONS = 50000
            # list of squares to test with
            allRings = [house.ringboundary for house in self.houses]

            while(True):

                # make iteration upper bound
                if relocateCounter > MAX_ITERATIONS:
                    print("Cannot place house...")
                    return 1
                # check if the h's house boundary is touching any existing ringboundary
                if h.boundary.isTouching(allRings):
                    # incorrect placement
                    relocateCounter += 1
                    h = (House(aType, "random", addRings))
                else:
                    # correct placement
                    self.houses.append(h)
                    print("Times Relocated: ", relocateCounter)
                    break

    """
    Expand all rings to their maximum possible value.
    """
    def expandRings(self):

        # NOTE this code might also work with coordinate distances, distance to edge etc, and then floor() the minimal answer

        print("\n Expanding rings...")

        # make a new list of houses
        newHouses = []

        # per imbedded house
        for house in self.houses:
            # TODO do while loop?????
            houses = self.houses

            # count number of rings added
            added_rings = []

            # make new house with 1 more ring
            hCurrent = house
            hNew = (House(house.type, house.origin, house.addRings + 1))

            # save boundaries of all embedded houses
            allBoundaries = [testhouse.boundary for testhouse in self.houses if testhouse.origin != house.origin]

            # the new ring is valid when its completely within map boundaries,
            # and not any house can be touching this new ringboundary
            # hNew.ringboundary.isWithin(self.boundary) and
            while(not any([houseboundary.isTouching(hNew.ringboundary)
                            for houseboundary in allBoundaries])):
                # if new ring is possible, replace hCurrent with hNew, and repeat
                added_rings.append(hNew.addRings)

                hCurrent = hNew
                hNew = (House(hCurrent.type, hCurrent.origin, hCurrent.addRings + 1))

            # if it is not possible, quit loop
            print("\n rings added: ", added_rings)
            newHouses.append(hCurrent)

        # after all looping:
        self.houses = newHouses


    """
    Add water to the map.
    """
    def addWater(self):

        waterArea = WATER_PERCENTAGE * AREA[0] * AREA[1]

        """
        # ingredients
        WATER_PERCENTAGE = 0.20         # percentage of total area covered by water
        MAX_BODIES       = 4            # maximum number of bodies
        MAX_RATIO        = 4            # l/b < x AND  b/l < x
        Rectangle()
        self.waterBody = []
        """


        """
        pseudo

        iterate with a body of water
            if fitting in loop times out,
                change aspect ratio
                    if aspect ratio cant be changed any longer
                        repeat entire thing with 2 bodies of water


        ? when do i try smaller squares / rectangles
        """
        # print()
        print("\nadding water...")
        print(waterArea)

    """
    Determine the value of the land.
    """
    def calculateValue(self):
        total = 0
        # per house
        for house in self.houses:
            # add house's cumulative value of the current ring
            total += house.ring.cumValue

        return total


    def save(self):

        file_name = "Saves/" + str(self.calculateValue()) + ".csv"
        with open(file_name , "w"):
            locationList = []
            for house in self.houses:
                row = [house.origin[0], house.origin[1], house.type.name]
                locationList.append(row)
            writer = pandas.DataFrame(locationList, columns=["x-co-ordinate", "y-co-ordinate", "house-type"])
            writer.to_csv(file_name, index=False)
            print("location list" + str(locationList))
    """
    plot the full map with all houses. This code is hard to understand
    without understanding the mathplot.py libaries
    """

    def plot(self):
        # init figure and axes
        fig = plt.figure()
        ax = fig.add_subplot(111, aspect = 'equal')

        # get rectangle information out of houses
        houseBound_list = []
        ringBound_list  = []
        for house in self.houses:
            rec1 = mathplot_rectangle(house.boundary.coord1, house.boundary.width, house.boundary.height, 0, fc=house.type.colour)
            rec2 = mathplot_rectangle(house.ringboundary.coord1, house.ringboundary.width, house.ringboundary.height, 0, fc=house.type.colour, alpha=0.2)
            ax.add_patch(rec1)
            ax.add_patch(rec2)

        # EXAMPLE FOR PROPERTIES
        # rect = patches.Rectangle((50,100),40,30,linewidth=1,edgecolor='r',facecolor='none')

        # determines how axis are drawn
        ax.set_xticks(np.arange(0, self.width, 10))
        ax.set_yticks(np.arange(0, self.height, 10))
        ax.set_xlim([0, self.width])
        ax.set_ylim([0, self.height])

        # draw the board
        plt.show()



