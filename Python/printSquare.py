"""
NAME    printSquare

AUTHORS Christiaan Wewer
        Tara Elsen
        jos feenstra        1196 95

DESC    STATE SPACE estimation calculation

NOTE    this thing is an example of how to use helpers
"""

<<<<<<< HEAD:Python/printSquare.py
from Python.helpers import *

# choose 0, 1 or 2 to get 20, 40 or 60 houses
SELECTED_HOUSE_COUNT = HOUSE_COUNT[2]

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
=======

# TODO turn main into hillclimber
# TODO save all values generated in .txt file
# TODO make an algoritm which determines which ring is the most valuable to add, with value in price / m2


from helpers import *

# choose 0, 1 or 2 to get 20, 40 or 60 houses
SELECTED_HOUSE_COUNT = HOUSE_COUNT[0]
>>>>>>> 1497b12e60cc4eb8241aa5f91612489838e80eac:printSquare.py


"""
build a correct random map
"""
def main():
    housetypes = initHouseTypes(20)

    # generate correct type parameters
    housetypelist = []
    for ht in housetypes:
        n = round(ht.frequency * SELECTED_HOUSE_COUNT)
        housetypelist += [ht] * n

    houstypelist = shuffle(housetypelist)
    print(housetypelist)

    # make a map
    map1 = Map()

    # add a number of houses to map
    for i in range(SELECTED_HOUSE_COUNT):

        # get current housetype
        ht = housetypelist[i]

        # the add house function which i want
        map1.addHouse(ht, (0,0), 10, "non_colliding", "random_positions")

    map1.plot()

    # make change all rings to its largest possible iteration
    map1.expandRings()

    # print value of map
    value = map1.calculateValue()
    print("Total map value:", value)

    # draw the map
    map1.plot()

if __name__ == "__main__":
<<<<<<< HEAD:Python/printSquare.py
    main2()












    # # example move
    # someVector = (100, 100)
    # someHouse.move(someVector)
    # print(someHouse.coord)


# questions about the case:
# can we turn bungalows & maisons ?
# can we
=======
    main()
>>>>>>> 1497b12e60cc4eb8241aa5f91612489838e80eac:printSquare.py
