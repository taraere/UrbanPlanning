"""
NAME    printSquare

AUTHORS Christiaan Wewer
        Tara Elsen
        jos feenstra        1196 95

DESC    STATE SPACE estimation calculation

NOTE    this thing is an example of how to use helpers
"""

from helpers import *

# choose 0, 1 or 2 to get 20, 40 or 60 houses
SELECTED_HOUSE_COUNT = HOUSE_COUNT[0]

"""
build a hardcoded sollution
"""
def main():
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





"""
build a random sollution
"""
def main2():
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
build a correct random sollution
"""
def main3():
    housetypes = initHouseTypes(20)

    # generate hosue parameteres
    housetypelist = []
    for ht in housetypes:
        n = round(ht.frequency * SELECTED_HOUSE_COUNT)
        housetypelist += [ht] * n

    houstypelist = shuffle(housetypelist)
    print(housetypelist)

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




def main4():
    housetypes = initHouseTypes(20)


if __name__ == "__main__":
    main()












    # # example move
    # someVector = (100, 100)
    # someHouse.move(someVector)
    # print(someHouse.coord)


# questions about the case:
# can we turn bungalows & maisons ?
# can we
