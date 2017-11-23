"""
NAME    printSquare

AUTHORS Christiaan Wewer
        Tara Elsen
        jos feenstra        1196 95

DESC    STATE SPACE estimation calculation

NOTE    this thing is an example of how to use helpers
"""
"""
HEURISTICS NOTES

prefer placing houses with the same type together
    prefer placing houses which perfectly fit together
prefer placing houses on edges of other houses or water
prefer placing houses so they fit perfectly in AREA boundaries
prefer to place as much 'extra free space' off the edge of the AREA boundaries

group houses, consider them as 1 (moldable) puzzle piece

"""

# TODO turn main into hillclimber
# TODO save all values generated in .txt file
# TODO make an algoritm which determines which ring is the most valuable to add, with value in price / m2


from helpers import *

# choose 0, 1 or 2 to get 20, 40 or 60 houses
SELECTED_HOUSE_COUNT = 30 # HOUSE_COUNT[0]


"""
build a correct random map
"""
def main():
    housetypes = initHouseTypes(100)

    # generate correct type parameters
    housetypelist = []
    for ht in reversed(housetypes):
        n = round(ht.frequency * SELECTED_HOUSE_COUNT)
        housetypelist += [ht] * n

    # make a map
    map1 = Map()

    # add a number of houses to map
    for i in range(SELECTED_HOUSE_COUNT):

        # get current housetype
        ht = housetypelist[i]

        # the add house function which i want
        map1.addHouse(ht, (0,0), 10, "random_positions", "non_colliding")

    # add water to the map (TODO)
    map1.addWater()

    map1.expandRings()
    #
    # # keep increasing the best house
    # for i in range(100):
    #     selected = map1.findHouseWithMostLandValueRingIncrease()
    #     map1.house[selected].changeRingsBy(1)
    #     # if that house does not fit
    #     while(not house[selected].isCorrect()):
    #         house[selected].relocate("random")
    #         relocatecounter += 1
    #         if relocatecounter > 1000:
    #             break




    # print value of map
    value = map1.calculateValue()
    print()
    print("Total map value:", value)

    # draw the map a second time
    map1.plot()

if __name__ == "__main__":
    main()
