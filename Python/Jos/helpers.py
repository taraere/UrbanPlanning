"""
NAME    ringPriorities

AUTHOR  jos feenstra

DESC    Contains Class information which represents the datastructure.

NOTE    the minimum distance to another home is represented by the name "ring",
        as its boundary representations look like square rings.

NOTE    isTouching()


// TODO implement map.save() & map.load()






"""
#import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle as mathplot_rectangle
import numpy as np
from random import randint, shuffle, random, randrange, choice, uniform
from collections import Iterable
import operator

# constances general
AREA = (160, 180)
HOUSE_COUNT = [20, 40, 60]

# water
WATER_PERCENTAGE = 0.20         # percentage of total area covered by water
MAX_BODIES       = 4            # maximum number of bodies
MAX_RATIO        = 4            # l/b < x AND  b/l < x

# house constances
NAME           = ["Family",  "Bungalow", "Mansion"  ]
FREQUENCY      = [0.60,      0.25,       0.15       ]
VALUE          = [285000,    399000,     610000     ]
SITE           = [(8, 8),    (10, 7.5),  (11, 10.5 )]
BASE_RING      = [2,         3,          6,         ]
RING_INCREMENT = [0.03,      0.04,       0.06       ]
COLOUR         = ["r",       'g',        'y'        ]
INTEGER        = [0,         1,          2          ]

################################################################################
"""
Housetype Class
"""

# TODO bouw water

class HouseType:

    def __init__(self, aName, aFrequency, aValue, aSite, aBaseRing, aRingIncrement, MaxRingIt, aColour, anInteger):

        # base values
        self.integer   = anInteger
        self.name      = aName
        self.frequency = aFrequency
        self.value     = aValue
        self.site      = aSite
        self.baseRing  = aBaseRing
        self.ringInc   = aRingIncrement
        self.colour    = aColour

        # calculated values
        self.width     = self.site[0]
        self.height    = self.site[1]
        self.area      = self.width * self.height
        self.landValue = self.value / self.area
        self.ringValue = round(self.ringInc * self.value)

        # do not calculate rings if the basering is incorrect
        if self.baseRing - 1 < 0:
            raise print("ERROR: Ring Creation Error")

        # instanciate cummulative variables
        cumArea        = self.area
        cumValue       = self.value
        cumLandValue   = self.landValue

        # fill ring list with Ring objects
        class Ring:
            pass
        self.ring = list()

        # iterate starting from basering, ending at Max Ring Iteration
        for ringWidth in range(self.baseRing, MaxRingIt):

            # turn r into Ring object
            r = Ring()

            # calc land value in € / m2, and calc other attributes
            r.ringWidth = ringWidth                  # synoniem
            r.x = ringWidth * 2 + self.width
            r.y = ringWidth * 2 + self.height
            r.area = r.x * r.y - cumArea

            # the first ring is part of the house, so it yields no value
            r.value = 0
            if ringWidth != self.baseRing:
                r.value = self.ringValue
            r.landValue = round(r.value / r.area, 1)

            # increase the cummilative values, and add the current values to r
            cumArea += r.area
            r.cumArea = cumArea

            cumValue += r.value
            r.cumValue = cumValue

            cumLandValue = round(cumValue / cumArea)
            r.cumLandValue = cumLandValue

            # add Ring object r to list ring
            self.ring.append(r)

    def printRingInfo(self):
        print()
        print(self.name)
        printstr = "| ring: {:2}   x: {:2}   y: {:3}   area: {:5}  landValue: {:5}  cumArea: {:6}  cumValue: {:7}   cumLandValue: {:5} |"
        print((len(printstr) - 4) * "-")
        for r in self.ring:
            print(printstr.format(r.ringWidth, r.x, r.y, r.area, r.landValue, r.cumArea, r.cumValue, r.cumLandValue ))
        print((len(printstr) - 4) * "-")

################################################################################
"""
House Class
"""
class House:

    def __init__(self, aType, aCoord, addRings):
        self.type = aType
        self.addRings = addRings

        # calc house's lower- and upperbounds of x and y coordinates
        # TODO these should be calculated in houseType
        self.xLower = self.type.ring[0].ringWidth
        self.yLower = self.type.ring[0].ringWidth
        self.xUpper = AREA[0] - self.type.ring[0].ringWidth - self.type.width
        self.yUpper = AREA[1] - self.type.ring[0].ringWidth - self.type.height

        # assign either a random coordinate, or assign given coordinate
        if aCoord == "random":
            # randomize numbers, with 0.5 precision
            random_x = round(uniform(self.xLower, self.xUpper) * 2) / 2
            random_y = round(uniform(self.yLower, self.yUpper) * 2) / 2

            self.origin = (random_x, random_y)
        else:
            self.origin = aCoord

        # update geometic info
        self.update()

    def update(self):
        # calculate additional geometric information, based on init's current value
            # EXAMPLE a fam.house with 3 add.rings gives a ringWidth of 5.

        # select current ring
        self.ring = self.type.ring[self.addRings]

        # house geometry rep. boundary
        self.boundary = Rectangle(self.origin, self.type.width, self.type.height)

        # move houseOrigin diagonal to create ringOrigin
        vector = (-1 * self.ring.ringWidth, -1 * self.ring.ringWidth)
        ringOrigin = moveCoord(self.origin, vector)

        # house ring rep. boundary
        self.ringboundary = Rectangle(ringOrigin, self.ring.x, self.ring.y)

        # make some synonimes for lazy use
        self.coord = self.origin

    def move(self, vector):

        # add vector and origin coordinate, and update other values accordingly
        self.origin = moveCoord(self.origin, vector)
        self.update()

    def moveTo(self, newCoord):

        # replace origin coordinate, and update other values accordingly
        self.origin = newCoord
        self.update()

        # change the |Additional Ring| value by |Increment|, error if addrings becomes negative (not allowed)
    def changeRingsBy(self, increment):
        # quit if addRings would become negative
        if self.addRings + increment < 0:
            print("ERROR: additional rings cannot become negative")
            return

        # add the increment, and update values
        self.addRings += increment
        self.update()

###############################################################################

"""
rectangle class

Methods:
toString()                              # turn self. information into string
isTouching(|rectangle / rectangles|)    # test if self is touching ||
isWithin(|rectangle / rectangles|)      # test if self is completely within ||
"""
class Rectangle:

    def __init__(self, OriginCoord, width, height):

        self.width = width
        self.height = height

        self.x1 = OriginCoord[0]
        self.y1 = OriginCoord[1]
        self.coord1 = (self.x1, self.y1)

        self.x2 = self.x1 + width
        self.y2 = self.y1 + height
        self.coord2 = (self.x2, self.y2)

        # get self' 4 boundary coordinates
        self.bound_coords = [(x, y) for x in [self.x1, self.x2]
                                    for y in [self.y1, self.y2]]

    # turn some of rectangles variables to string to test
    def toString(self):
        return ("Rectangle.coord1: {} \n Rectangle.coord2: {} \n".format(
               self.coord1,
               self.coord2)
               )
    # return true if self is touching any part of list of rectangles
    def isTouching(self, listOfRectangles):

        # TODO make it so a single rectangle also works
        if not isinstance(listOfRectangles, Iterable):
            listOfRectangles = [listOfRectangles]

        # calculate per boundary coordinate
        for bound_coord in self.bound_coords:
            # per rectangle in given list of rectangles
            for rec in listOfRectangles:

                # rename bound coord for the sake of clear names
                x = bound_coord[0]
                y = bound_coord[1]
                # print(bound_coord)
                # print(rec.x1, rec.x2, rec.y1, rec.y2)
                # print(rec.x1 < x < rec.x2 and rec.y1 < y < rec.y2)
                # if self. boundary coord is inside of rec. boundaries
                if rec.x1 < x < rec.x2 and rec.y1 < y < rec.y2:
                    return True

                # test the other way around
                for rec_bound in rec.bound_coords:

                    # if rec. boundary coord is within self. boundaries
                    if self.x1 < rec_bound[0] < self.x2 and self.y1 < rec_bound[1] < self.y2:
                        return True

        # if code falls down till this part, none of the rectangles are touching self
        return False

    # return true if self is completely within list of rectangles
    def isWithin(self, listOfRectangles):

        # get self' 4 boundary coordinates
        bound_coords = [(x, y) for x in [self.x1, self.x2]
                               for y in [self.y1, self.y2]]

        # TODO make it so a single rectangle also works
        if not isinstance(listOfRectangles, Iterable):
            listOfRectangles = [listOfRectangles]

        # calculate per boundary coordinate
        for bound_coord in bound_coords:
            # per rectangle in given list of rectangles
            for rec in listOfRectangles:

                # rename bound coord for the sake of clear names
                x = bound_coord[0]
                y = bound_coord[1]

                # test conditions
                if not rec.x1 <= x < rec.x2 or not rec.y1 <= y < rec.y2:
                    return False

        # if code falls down till this part, position is correct
        return True


###############################################################################

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
        self.house = []
        houseIndex = 0
        self.waterBody = []

        # init a boundary for collision testing
        self.boundary = Rectangle(self.coord1, self.width, self.height)

    """
    add a [aType] house to the map at [aCoord], with [addrings] rings
    """
    def addHouseStupid(self, aType, aCoord, addRings):
        # simple way of creating a house
        self.house.append(House(aType, aCoord, addRings))

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
            print()
            print("make a house without colliding")
            LoopUntilValid = True
        if any(option == "random_positions" for option in options):
            print("make house at a random location")
            h = (House(aType, "random", addRings))
        else:
            print("make a house in ordinary fashion")
            h = (House(aType, aCoord, addRings))

        # directly append h if we dont need to check for valid position
        if not LoopUntilValid:
            self.house.append(h)
        else:
            # if we do need to check if placement is valid
            relocateCounter = 0
            MAX_ITERATIONS = 50000
            # list of squares to test with
            allRings = [house.ringboundary for house in self.house]

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
                    self.house.append(h)
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

        # per imbedded hosue
        for house in self.house:
            # TODO do while loop?????
            houses = self.house

            # count number of rings added
            added_rings = []

            # make new house with 1 more ring
            hCurrent = house
            hNew = (House(house.type, house.origin, house.addRings + 1))

            # save boundaries of all embedded houses
            allBoundaries = [testhouse.boundary for testhouse in self.house if testhouse.origin != house.origin]

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

        # after all loopnig:
        self.house = newHouses


    """
    Add water to the map.
    """
    def addWater(self):

        # TODO MAKE WATER FIT
        # waterArea = WATER_PERCENTAGE * AREA[0] * AREA[1]
        # print()
        # print("adding water...")
        # print(waterArea)

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

    """
    Determine the value of the land.
    """
    def calculateValue(self):
        total = 0
        # per house
        for house in self.house:
            # add house's cummilative value of the current ring
            total += house.ring.cumValue

        return total

    """
    plot the full map with all houses. This code is hard to understand
    without understanding the mathplot.py libaries
    """
    def plot(self):

        # TODO maybe draw borers

        # init figure and axes
        fig = plt.figure()
        ax = fig.add_subplot(111, aspect='equal')

        # get rectangle information out of houses
        houseBound_list = []
        ringBound_list  = []
        for house in self.house:
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



    """ tara is on the case! """
    def load():
        # TODO
        pass
    def save():
        # TODO
        pass

    """
    USAGE

    selected =
    or
    selected = map.findHouseWithMostValueRingIncrease()

    map.house[selected].AddRings(1)


    """
    def findHouseWithMostLandValueRingIncrease(self):

        housedata = []
        # iterate through houses
        for index, house in enumerate(self.house):
            # get the landValue of the next ring
            pair = (house.type.ring[house.addRings + 1].landValue, index)

            # add data to list
            housedata.append(pair)

        # sort
        print(housedata)
        selected_house = max(housedata, key=operator.itemgetter(0))
        print(selected_house)

        return selected_house[1]






###############################################################################
"""
This area is for functions with are no part of classes
"""


"""
instantiate the 3 housetype objects
"""
def initHouseTypes(IterationMax=20):
    # determines how many rings will be added and calculated
    maximumRingIterations = IterationMax

    # make a list of House objects
    houseTypeList = list()
    for i,s in enumerate(NAME):
        houseTypeList.append(
            HouseType(NAME[i], FREQUENCY[i], VALUE[i], SITE[i], BASE_RING[i],
                RING_INCREMENT[i], maximumRingIterations, COLOUR[i], INTEGER[i])
        )
    return houseTypeList



"""
add a coordinate and a vector (movement representative) together
- make a coordinate class/?????
"""
def moveCoord(coordinate, vector):
    return tuple(sum(x) for x in zip(coordinate, vector))







# increase best ring of list of houses
# returns the [i] of the houselist which needs a ring increase




















"""
################################################################################
All of this stuff is junk, but it might be useful to show previous versions of
the code
################################################################################
:
"

class Coord(tuple):

    def __new__(cls, width, height):
        return tuple.__new__(cls, (width, height)) # create tuple with 2 items

    def __init__(self, x, y):
        self.x = y # width is the first argument passed
        self.y = y # height is the next



# or WAAAAYYY easier

from collections import namedtuple

Coord = namedtuple("Coord", ('x', 'y'))

# does not allow additional stuff like
coord1.move
coord1.moveto
coord1.plot


# example
coord1 = Coord(20, 40)
print(coord1)
>>> (20, 40)
print(coord1.x)
>>> 20
print(coord1.y)
>>> 40




onze case/????////// na 2e college
we moeten depth first gaan!!!!!!!
daarom eerst 1 groot apparaat maken, dan kleinere
[9][3][2][1]
[9][][][]




        # make clearer var names
        x = h.origin[0]
        y = h.origin[1]

        # push the house within bounds if the house is outside of bounds
        if x <  h.xLower:
            x = h.xLower
        if y <  h.yLower:
            y = h.yLower
        if x >= h.xUppers:
            x = h.xUpper
        if y >= h.yUpper:
            y = h.yUpper




















    # # example move
    # someVector = (100, 100)
    # someHouse.move(someVector)
    # print(someHouse.coord)


# questions about the case:
# can we turn bungalows & maisons ?
# can we
################################################################################

"
build a hardcoded map
"
def main_old1():
    ht = initHouseTypes(20)

    # example house object values
    hType = [ht[0], ht[2], ht[0], ht[1], ht[2], ht[0], ht[2], ht[0], ht[1], ht[2]]
    coordinate = [(50, 50), (64, 21), (54, 50), (84, 97), (12, 23), (45, 56), (100, 100), (30, 30), (200, 54)]
    ringsToAdd = [3, 3, 6, 4, 7, 8, 9, 3, 0, 0]

    # make a map
    map1 = Map()

    # fill the map
    for i in range(9):
        map1.addHouse(hType[i], coordinate[i], ringsToAdd[i])


    something = map1.house[1].boundary.height
    print(something)

    # draw the map
    map1.plot()



build a random map

def main_old2():
    housetypes = initHouseTypes(20)

    # generate hosue parameteres
    housetypelist = []
    for housetype in housetypes:
        n = round(housetype.frequency * SELECTED_HOUSE_COUNT)
        housetypelist += [housetype] * n

    # houstypelist = shuffle(housetypelist)

    # make a map
    map1 = Map()

    # add houses to map
    for i in range(SELECTED_HOUSE_COUNT):

        # create other parameters
        coordinate = (randint(0, AREA[0]-1), randint(0, AREA[1]-1))
        ringsToAdd = randint(1, 12)

        # add house
        map1.addHouse(housetypelist[i], coordinate, ringsToAdd)

    # draw the map
    map1.plot()




"""
