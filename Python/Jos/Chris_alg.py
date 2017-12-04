"""
NAME    printSquare

AUTHORS Christiaan Wewer
        Tara Elsen
        jos feenstra        1196 95

DESC    STATE SPACE estimation calculation

NOTE    this thing is an example of how to use helpers
"""


# TODO turn main into hillclimber
# TODO save all values generated in .txt file
# TODO make an algoritm which determines which ring is the most valuable to add, with value in price / m2


from helpers import *

# choose 0, 1 or 2 to get 20, 40 or 60 houses
SELECTED_HOUSE_COUNT = HOUSE_COUNT[0]


"""
build a correct random map
"""
def main0():
    housetypes = initHouseTypes(50)

    # generate correct type parameters
    housetypelist = []
    for ht in reversed(housetypes):
        n = round(ht.frequency * SELECTED_HOUSE_COUNT)
        housetypelist += [ht] * n

    # make a map
    map1 = Map()

    xAdd = int(map1.width/5)
    yAdd = int(map1.width/4)



    count = 0;
    # add a number of houses to map
    for i in range(5):

        for j in range (4):
            # get current housetype
            ht = housetypelist[count]
            count += 1
            # print(i, j, i * j)
            # the add house function which i want
            map1.addHouse(ht, (j * xAdd,i * yAdd), 0)



    # add water to the map
    map1.addWater()

    # make change all rings to its largest possible iteration
    map1.expandRings()

    # print value of map
    value = map1.calculateValue()
    print()
    print("Total map value:", value)

    # draw the map a second time
    map1.plot()

def main2():
    housetypes = initHouseTypes(50)

    # generate correct type parameters
    housetypelist = []
    for ht in reversed(housetypes):
        n = round(ht.frequency * SELECTED_HOUSE_COUNT)
        housetypelist += [ht] * n

    # make a map
    map1 = Map()



    # algorithm that gets optimal grid dimensions
    count = 1;
    while (True):
        check = SELECTED_HOUSE_COUNT % count
        if check == 0 and SELECTED_HOUSE_COUNT/count <= count:
            y = count
            break
        count += 1
    x = int(SELECTED_HOUSE_COUNT/y)

    # create baseplot
    xAdd = 0
    # yAdd = 0
    ringsadded = 0

    for house in range(x):

        # if functie voor kijken welke ringwidth het beste is (house of house + 1

        ht = housetypelist[house]

        # print(ht.ring[ringsadded].ringWidth, ht2.ring[ringsadded].ringWidth, ht.width)
        ringWidth = ht.ring[ringsadded].ringWidth



        if house < 1:
            xAdd += ringWidth
            # yAdd += ringWidth
        else:
            # yAdd += ringWidth + ht.height

            ht2 = housetypelist[house - 1]

            if ht.ring[ringsadded].ringWidth > ht2.ring[ringsadded].ringWidth:
                xRingSpace = ht.ring[ringsadded].ringWidth * 2
            elif ht.ring[ringsadded].ringWidth == ht2.ring[ringsadded].ringWidth:
                xRingSpace = ht.ring[ringsadded].ringWidth
            else:
                xRingSpace = ht2.ring[ringsadded].ringWidth

            xAdd += xRingSpace + ht.width

        print('\n', xAdd, ringWidth)
        map1.addHouse(ht, (xAdd, ringWidth), 0)



        # map1.expandRings()

        # map1.house[0].ring.ringWidth




#UGLY SHIT

    # count = 0;
    # # add a number of houses to map
    # for i in range(y):
    #
    #     for j in range (x):
    #         # get current housetype
    #         ht = housetypelist[count]
    #         count += 1
    #         # print(i, j, i * j)
    #         # the add house function which i want
    #         map1.addHouse(ht, (j * xAdd,i * yAdd), 0)



    # add water to the map
    # map1.addWater()

    # make change all rings to its largest possible iteration
    # map1.expandRings()

    # print value of map
    value = map1.calculateValue()
    print()
    print("Total map value:", value)

    # draw the map a second time
    map1.plot()

# def addThisMfkingHouse():
#     #jh

def main3():
    housetypes = initHouseTypes(50)

    # generate correct type parameters
    housetypelist = []
    for ht in reversed(housetypes):
        n = round(ht.frequency * SELECTED_HOUSE_COUNT)
        housetypelist += [ht] * n

    # make a map
    map1 = Map()

    # algorithm that gets optimal housegrid dimensions
    count = 1;
    yHouses = 0
    while (True):
        check = SELECTED_HOUSE_COUNT % count
        if check == 0 and SELECTED_HOUSE_COUNT/count <= count:
            yHouses = count
            break
        count += 1
    xHouses = int(SELECTED_HOUSE_COUNT/yHouses)




    print(yHouses, xHouses)
    htMin = housetypelist[19]

    minDistance = htMin.ring[0].ringWidth + htMin.width
    minFirstDistance = htMin.ring[0].ringWidth

    x = htMin.ring[0].ringWidth
    y = htMin.ring[0].ringWidth

    # housecounter
    houseCounter = 0

    # loop through x houses
    for xHouse in range(xHouses):

        # loop through y houses
        for yHouse in range(yHouses):

            # get house from housecounter
            ht = housetypelist[houseCounter]

            # add houses
            map1.addHouse(ht, (x, y), 0)


            allhouses = [h.boundary for h in map1.house]

            # check if is touching
            # hoe pak ik hier die istouching functie dan?


            curHouse = map1.house[houseCounter]
            houseCounter += 1
            check = curHouse.ringboundary.isTouching(allhouses) #dit klopt niet

            # while(check):


            print("ringboundary", check)
            # increment y
            y += minDistance
        # increment x
        x += minDistance

        # reset y
        y = htMin.ring[0].ringWidth





    map1.plot()

if __name__ == "__main__":
    main3()
