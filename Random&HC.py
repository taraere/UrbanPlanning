"""
NAME    Random is cool

AUTHORS Christiaan Wewer

DESC    MAKING THE MAP DANCE

"""


from helpers import *
from random import randint
import matplotlib.pyplot as plt
import sys

# choose 0, 1 or 2 to get 20, 40 or 60 houses
SELECTED_HOUSE_COUNT = 20 # HOUSE_COUNT[0]


def hillclimberTwoHouses(usedMap, maxIterations, xValues, yValues):

    for iteration in range(maxIterations):

        # calculate mapvalue
        mapValue = usedMap.calculateValue()
        print("mapvalue: " + str(mapValue))

        # get two random houses
        randHouseIntOne = randint(0, len(usedMap.house) - 1)
        randHouseIntTwo = 0

        # check if its not the same house
        while True:
            randHouseIntTwo = randint(0, len(usedMap.house) - 1)
            if randHouseIntOne != randHouseIntTwo:
                break

        swapHouses(usedMap, randHouseIntOne, randHouseIntTwo)

        # calculate value
        mapValueAfter = usedMap.calculateValue()
        print("mapvalue After: " + str(mapValueAfter))

        # check if map is valid and if not undo
        if not usedMap.house[randHouseIntOne].ringboundary.isWithin(usedMap.boundary) or not usedMap.house[randHouseIntTwo].ringboundary.isWithin(usedMap.boundary) or mapValueAfter < mapValue:
            swapHouses(usedMap, randHouseIntTwo, randHouseIntOne)
            yValues.append(mapValue)
            print("you suckahh algorithm, swap it back")

        else:
            yValues.append(mapValueAfter)

        print()

        # append xValues
        xValues.append(iteration)


def swapHouses(usedMap, houseIntOne, houseIntTwo):

    # swap houses
    coord1 = usedMap.house[houseIntOne].origin
    coord2 = usedMap.house[houseIntTwo].origin
    usedMap.house[houseIntOne].relocate(coord2)
    usedMap.house[houseIntTwo].relocate(coord1)


def hillclimberRandomRelocateRecursive(usedMap, startCounter, maxIterations, relocateIterations, xValues, yValues):

    # calculate mapvalue
    mapValue = usedMap.calculateValue()
    print("mapvalue before: " + str(mapValue))

    # get random house
    randHouseInt = randint(0, len(usedMap.house) - 1)

    # get coordinates from house randHouseInt
    coord1 = usedMap.house[randHouseInt].origin

    usedMap.house[randHouseInt].relocate("random")

    # calculate value of map after new relocation
    mapValueAfter = usedMap.calculateValue()

    print(mapValueAfter)

    # replaces house if necessary
    if mapValueAfter < 0:
        counterForRelocation = 0
        while mapValueAfter < 0:
            usedMap.house[randHouseInt].relocate("random")
            mapValueAfter = usedMap.calculateValue()
            counterForRelocation += 1
            if counterForRelocation > relocateIterations:
                usedMap.house[randHouseInt].relocate(coord1)
                mapValueAfter = usedMap.calculateValue()

    if mapValueAfter <= mapValue:
        print("map is not better")
        usedMap.house[randHouseInt].relocate(coord1)
        mapValueAfter = usedMap.calculateValue()
        print("new value after relocate: {}".format(str(mapValueAfter)))

    startCounter += 1

    yValues.append(mapValueAfter)
    xValues.append(startCounter)

    # calculate value
    print("mapvalue After: " + str(mapValueAfter))

    print()

    if startCounter >= maxIterations:
        return usedMap
    else:
        return hillclimberRandomRelocateRecursive(usedMap, startCounter, maxIterations, relocateIterations, xValues, yValues)


def hillclimberRandomRelocate(usedMap, maxIterations, relocateIterations, xValues, yValues):

    for startCounter in range(maxIterations):
        # calculate mapvalue
        mapValue = usedMap.calculateValue()
        print("mapvalue before: " + str(mapValue))

        # get random house
        randHouseInt = randint(0, len(usedMap.house) - 1)

        # get coordinates from house randHouseInt
        coord1 = usedMap.house[randHouseInt].origin

        usedMap.house[randHouseInt].relocate("random")

        # calculate value of map after new relocation
        mapValueAfter = usedMap.calculateValue()

        print(mapValueAfter)

        # replaces house if necessary
        if mapValueAfter < 0:
            counterForRelocation = 0
            while mapValueAfter < 0:
                usedMap.house[randHouseInt].relocate("random")
                mapValueAfter = usedMap.calculateValue()
                counterForRelocation += 1
                if counterForRelocation > relocateIterations:
                    usedMap.house[randHouseInt].relocate(coord1)
                    mapValueAfter = usedMap.calculateValue()

        if mapValueAfter <= mapValue:
            print("map is not better")
            usedMap.house[randHouseInt].relocate(coord1)
            mapValueAfter = usedMap.calculateValue()
            print("new value after relocate: {}".format(str(mapValueAfter)))

        yValues.append(mapValueAfter)
        xValues.append(startCounter)

        # calculate value
        print("mapvalue After: " + str(mapValueAfter))

        print()


def randomMapAlgorithm(tries, houseTypeList, xValues, yValues):

    # initialize counter, map, fill map and get value
    counter = 0
    bestMap = Map()
    fillMapWithRandomNonCollidingHouses(bestMap, houseTypeList)
    bestMapValue = bestMap.calculateValue()

    while True:

        # make empty map and fill it
        emptyMap = Map()
        fillMapWithRandomNonCollidingHouses(emptyMap, houseTypeList)

        # calculate values of two maps
        emptyMapValue = emptyMap.calculateValue()

        print(counter, bestMapValue, emptyMapValue)
        counter += 1

        # check which map to keep
        if emptyMapValue > bestMapValue:

            bestMap = emptyMap
            bestMapValue = emptyMapValue

        yValues.append(bestMapValue)
        xValues.append(counter)

        # return if counter has reached the amount of tries
        if counter >= tries:
            return bestMap


def fillMapWithRandomNonCollidingHouses(usedMap, houseTypeList):

    # fill map with houses
    for i in range(SELECTED_HOUSE_COUNT):
        ht = houseTypeList[i]
        usedMap.addHouse(ht, (0, 0), 0, "random_positions", "non_colliding")

"""
build a correct random map
"""

def main():

    # set recursiondepth deeper
    sys.setrecursionlimit(10000)

    housetypes = initHouseTypes(100)

    # generate correct type parameters
    housetypelist = []
    for ht in reversed(housetypes):
        n = round(ht.frequency * SELECTED_HOUSE_COUNT)
        housetypelist += [ht] * n

    # make a map
    yValues1 = []
    yValues2 = []
    yValues3 = []
    xValues = []
    xValues1 = []
    xValues2 = []
    xValues3 = []

    map1 = randomMapAlgorithm(10, housetypelist, xValues1, yValues1)

    incrementValue = xValues1[-1]
    xValues2.append(incrementValue)
    yValues2.append(yValues1[-1])

    map1.plot()

    hillclimberRandomRelocate(map1, 20, 30, xValues, yValues2)

    map1.plot()

    for value in xValues:
        xValues2.append(value + incrementValue)
    xValues = []

    incrementValue = xValues2[-1]
    xValues3.append(incrementValue)
    yValues3.append(yValues2[-1])

    hillclimberTwoHouses(map1, 10, xValues, yValues3)

    for value in xValues:
        xValues3.append(value + incrementValue)

    map1.addWater()
    map1.plot()

    plt.plot(xValues3, yValues3)
    plt.plot(xValues2, yValues2)
    plt.plot(xValues1, yValues1)

    plt.ylabel("Price")
    plt.xlabel("Iterations")
    plt.title("Random Map Algorithm + Relocator Hillclimber + Houseswitcher Hillcllimber")
    plt.show()


    print()

    print(map1.calculateValue())

    value = map1.calculateValue()

    print()

    print("Total map value:", value)


if __name__ == "__main__":
        main()
