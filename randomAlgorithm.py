"""
NAME    printSquare

AUTHORS Tara Elsen

DESC    STATE SPACE estimation calculation

NOTE    this thing is an example of how to use helpers
"""
from Now.helpers import *

# choose 0, 1 or 2 to get 20, 40 or 60 houses
SELECTED_HOUSE_COUNT = HOUSE_COUNT[2]
RUN_ITERATIONS = 1

'''
move subtly along both axes
'''
def moveEachHouse(aMap):
    while aMap.calculateValue() < 35_000_000:
        value = aMap.calculateValue()
        for i in range(len(aMap.house)):
            # retrieve x and y co-ordinates
            aHouse = aMap.house[i]

            # move right
            moveHouse(aMap, aHouse, 0.5, 0)
            if goodMove(aMap, aHouse, value):
                break

            # move left
            moveHouse(aMap, aHouse, -1, 0)
            if goodMove(aMap, aHouse, value):
                break

            # move up
            moveHouse(aMap, aHouse, 0.5, 0.5)
            if goodMove(aMap, aHouse, value):
                break

            # move down
            moveHouse(aMap, aHouse, 0, -1)
            if goodMove(aMap, aHouse, value):
                break

        newValue = aMap.calculateValue()

        if newValue == value:
            break

    print("\n New map value:", aMap.calculateValue())

"""
check it's an improved move
"""
def goodMove(aMap, aHouse, oldValue):
    if aHouse.ringboundary.isWithin(aMap.boundary) and aHouse.boundary.isWithin(aMap.boundary):
        if compareValue(aMap, oldValue):
            return True

"""
compare values algorithm
"""
def compareValue(secondMap, value):
        newValue = secondMap.calculateValue();
        # calculate map and compare with last calculation
        # new version will
        if newValue > value:
            return True

"""
move house half a meter 
"""
def moveHouse(aMap, aHouse, x_change, y_change):
    x_coord = aHouse.origin[0]
    y_coord = aHouse.origin[1]

    # move
    x_coord += x_change
    y_coord += y_change
    aHouse.relocate((x_coord, y_coord))

"""
build a correct random map
"""
def main():
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
        print("value before" + str(value))
        fullMap.save("beforeBig")

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

        aMap.save("afterBig")
        aMap.expandRings()
        aMap.plot()

if __name__ == "__main__":
    main()


