"""
NAME    printSquare

AUTHORS Tara Elsen

DESC    STATE SPACE estimation calculation

NOTE    this thing is an example of how to use helpers
"""
from Now.helpers import *
from Now.classes import *

# choose 0, 1 or 2 to get 20, 40 or 60 houses
SELECTED_HOUSE_COUNT = HOUSE_COUNT[0]
RUN_ITERATIONS = 1

def moveEachHouse(aMap):
    '''
    move subtly along both axes
    '''
    iterations = 0
    sameValue = 0
    # inc = 128
    # inc = 64
    # inc = 32
    # inc = 16
    # inc = 8
    # inc = 4
    # inc = 2
    # inc = 1
    inc = 0.5
    while aMap.calculateValue() < 35_000_000:
        iterations += 1
        value = aMap.calculateValue()
        houseCount = len(aMap.house)

        for i in range(houseCount):
            # retrieve x and y co-ordinates
            aHouse = aMap.house[i]

            # move right
            moveHouse(aMap, aHouse, inc, 0)
            if goodMove(aMap, aHouse, value):
                print("move right")
                sameValue = 0
            else:
                moveHouse(aMap, aHouse, -inc, 0)

            # move upper-right
            moveHouse(aMap, aHouse, inc, inc)
            if goodMove(aMap, aHouse, value):
                print("move upper-right")
                sameValue = 0
            else:
                moveHouse(aMap, aHouse, -inc, -inc)

            # move lower-right
            moveHouse(aMap, aHouse, inc, -inc)
            if goodMove(aMap, aHouse, value):
                print("move lower-right")
                sameValue = 0
            else:
                moveHouse(aMap, aHouse, -inc, inc)

            # move left
            moveHouse(aMap, aHouse, -inc, 0)
            if goodMove(aMap, aHouse, value):
                print("move left")
                sameValue = 0
            else:
                moveHouse(aMap, aHouse, inc, 0)

            # move upper-left
            moveHouse(aMap, aHouse, -inc, inc)
            if goodMove(aMap, aHouse, value):
                print("move upper-left")
                sameValue = 0
            else:
                moveHouse(aMap, aHouse, inc, -inc)

            # move lower-left
            moveHouse(aMap, aHouse, -inc, -inc)
            if goodMove(aMap, aHouse, value):
                print("move lower-left")
                sameValue = 0
            else:
                moveHouse(aMap, aHouse, inc, inc)

            # move up
            moveHouse(aMap, aHouse, 0, inc)
            if goodMove(aMap, aHouse, value):
                print("move up")
                sameValue = 0
            else:
                moveHouse(aMap, aHouse, 0, -inc)

            # move down
            moveHouse(aMap, aHouse, 0, -inc)
            if goodMove(aMap, aHouse, value):
                print("move down")
                sameValue = 0
            else:
                moveHouse(aMap, aHouse, 0, inc)
                sameValue += 1
                print("sameValue is ", sameValue)

        newValue = aMap.calculateValue()

        if inc <= 0.5 and sameValue == houseCount:
            break

        if sameValue >= houseCount:
            inc /= 2
            print("incremented steps are ", inc)
            sameValue = 0

    print("\n New map value: ", aMap.calculateValue())

def goodMove(aMap, aHouse, oldValue):
    """
    check it's an improved move
    """
    if aHouse.ringboundary.isWithin(aMap.boundary) and aHouse.boundary.isWithin(aMap.boundary):
        if aHouse.origin[0] > 0 and aHouse.origin[1] > 0:
            if aHouse.origin[0] <= 180 and aHouse.origin[1] <= 160:
                if compareValue(aMap, oldValue):
                    return True
    return False

def compareValue(secondMap, value):
    """
    compare values algorithm
    calculate map and compare with last calculation
    """
    newValue = secondMap.calculateValue();
    if newValue > value:
        return True
    # else

def moveHouse(aMap, aHouse, x_change, y_change):
    """
    move house half a meter 
    """
    x_coord = aHouse.origin[0]
    y_coord = aHouse.origin[1]

    # move
    x_coord += x_change
    y_coord += y_change
    aHouse.relocate((x_coord, y_coord))

def increaseDistance(aMap, aHouse):
    """
    Try to increase distances between houses
    """
    aHouse.boundary.getShortestDistance()


def main():
    """
    build a correct random map
    """
    houseTypes = initHouseTypes(100)

    # generate correct type parameters
    houseTypeList = []
    for ht in reversed(houseTypes):
        n = round(ht.frequency * SELECTED_HOUSE_COUNT)
        houseTypeList += [ht] * n

    # make a map
    aMap = Map()

    # fill map for the first time
    for j in range(RUN_ITERATIONS):
        for i in range(SELECTED_HOUSE_COUNT):
            ht = houseTypeList[i]
            aMap.addHouse(ht, (0, 0), 0, "random_positions", "non_colliding")

        # initial value to compare to
        fullMap = aMap
        value = fullMap.calculateValue()
        print("value before: " + str(value))
        fullMap.saveJSON("/Users/Tara/Desktop/UrbanPlanning/Saves", str(value)+"_before1")

        # upper bound of all the routes houses could take
        # for k in range(factorial(160)*factorial(180)*2):
        # move every house half a meter in the direction of either axes
        moveEachHouse(aMap)

        '''
        choose direction that it can get the furthest in???
        Otherwise you always give preference to moving right - 
        solve this issue with taking the direction which goes the furthest
        
        Otherwise, check the proximity of all of the houses and move away from them
        '''

        aMap.saveJSON("/Users/Tara/Desktop/UrbanPlanning/Saves/", str(aMap.calculateValue())+"_inc1")
        aMap.plot()

if __name__ == "__main__":
    main()


