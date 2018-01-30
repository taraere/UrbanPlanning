from Rectangle import *

class House:
    """
    House Class
    
    Methods:
        update          Calculate additional geometric information, based on init's current value
                        EXAMPLE a fam.house with 3 add.rings gives a ringWidth of 5. 
        move            Add vector and origin coordinate, and update other values accordingly
        moveTo          Replace origin coordinate, and update other values accordingly
    """

    def __init__(self, aType, aCoord, addRings):
        self.type = aType
        self.addRings = addRings

        # select current ring
        self.ring = self.type.ring[self.addRings]

        # calc house's lower- and upperbounds of x and y coordinates
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

        # update geometric info
        self.update()

    def update(self):
        """ 
        calculate additional geometric information, based on init's current value
        EXAMPLE a fam.house with 3 add.rings gives a ringWidth of 5. 
        """

        # house geometry rep. boundary
        self.boundary = Rectangle(self.origin, self.type.width, self.type.height)

        # move houseOrigin diagonal to create ringOrigin
        vector = (-1 * self.ring.ringWidth, -1 * self.ring.ringWidth)
        ringOrigin = moveCoord(self.origin, vector)

        # house ring rep. boundary
        self.ringboundary = Rectangle(ringOrigin, self.ring.x, self.ring.y)

        # make some synonyms for lazy use
        self.coord = self.origin

    def move(self, vector):

        # add vector and origin coordinate, and update other values accordingly
        self.origin = moveCoord(self.origin, vector)
        self.update()

    def moveTo(self, newCoord):

        # replace origin coordinate, and update other values accordingly
        self.origin = newCoord
        self.update()