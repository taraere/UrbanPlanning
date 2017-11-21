from House import *
from HouseType import *

class Rectangle:
    """
    rectangle class
    
    Methods:
    toString()                              # turn self. information into string
    isTouching(|rectangle / rectangles|)    # test if self is touching ||
    isWithin(|rectangle / rectangles|)      # test if self is completely within ||
    """

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

        # if code falls down til this part, none of the rectangles are touching self
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
