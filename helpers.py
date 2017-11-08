"""
NAME    ringPriorities

AUTHOR  jos feenstra

DESC    STATE SPACE estimation calculation

NOTE    the minimum distance to another home is represented by the name "ring",
        as its boundary representations look like square rings.
"""
#import numpy as np


# constances general
AREA = (160, 180)
HOUSE_COUNT = [20, 40, 60]

# water (ignored for now)
WATER_PERCENTAGE = 0.20         # percentage of total area covered by water
MAX_BODIES       = 4            # maximum number of bodies
MAX_RATIO        = 4            # l/b < x AND  b/l < x

# house constances
NAME           = ["Family",  "Bungalow", "Mansion"   ]
FREQUENCY      = [60,        25,         15          ]
VALUE          = [285000,    399000,     610000      ]
SITE           = [(8, 8),    (10, 7.5),  (11, 10.5  )]
BASE_RING      = [2,         3,          6,          ]
RING_INCREMENT = [0.03,      0.04,       0.06        ]

# additional calculation values

################################################################################

# house class

"""
Housetype Class
"""
class HouseType:

    def __init__(self, aName, aFrequency, aValue, aSite, aBaseRing, aRingIncrement, MaxRingIt):

        # base values
        self.name      = aName
        self.frequency = aFrequency
        self.value     = aValue
        self.site      = aSite
        self.baseRing  = aBaseRing
        self.ringInc   = aRingIncrement

        # calculated values
        self.x         = self.site[0]
        self.y         = self.site[1]
        self.area      = self.x * self.y
        self.landValue = self.value / self.area
        self.ringValue = round(self.ringInc * self.value)

        # do not calculate rings if the basering is incorrect
        if self.baseRing - 1 < 0:
            raise print("ERROR: Ring Creation Error")

        # instanciate cummulative variables
        cumArea        = self.area
        cumValue       = self.value
        cumLandValue   = self.landValue

        # make array of rings and their weighted values
        class Ring:
            pass
        self.ring = list()

        # fill ring list with Ring objects
        for ringWidth in range(self.baseRing, MaxRingIt):

            # turn r into Ring object
            r = Ring()

            # calc land value in € / m2, and calc other attributes
            r.width = ringWidth
            r.ring = ringWidth                  # synoniem
            r.x = ringWidth * 2 + self.x
            r.y = ringWidth * 2 + self.y
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
            print(printstr.format(r.ring, r.x, r.y, r.area, r.landValue, r.cumArea, r.cumValue, r.cumLandValue ))
        print((len(printstr) - 4) * "-")



"""
House Class
"""
class House:

    def update(self):
        self.coord = self.origin
        # TODO ADD CORRECT RING COORDINATES AND MORE HOUSE GEOMETRY INFO

        # calculate additional geometric information, based on

    def __init__(self, aType, aCoord, ExtraRings):
        self.type = aType
        self.origin = aCoord
        self.rings = ExtraRings
        self.update(self)

    def move(self, vector):
        # example vector = (6, -1)
        self.origin = tuple(map(sum, zip(self.origin, vector))

        # change other values with this change
        self.update(self)

    def moveTo(self, newCoord):
        self.origin = newCoord

        # change other values with this change
        self.update(self)





###############################################################################


"""
instantiate all house objects
"""
def initHouseTypes(IterationMax=20):
    # determines how many rings will be added and calculated
    maximumRingIterations = IterationMax

    # make a list of House objects
    houseTypeList = list()
    for i,s in enumerate(NAME):
        houseTypeList.append(
            HouseType(NAME[i], FREQUENCY[i], VALUE[i], SITE[i], BASE_RING[i],
                RING_INCREMENT[i], maximumRingIterations)
        )
    return houseTypeList
