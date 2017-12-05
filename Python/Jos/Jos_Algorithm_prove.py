"""
NAME    jos's Algorithm

AUTHORS jos feenstra

DESC    MAKING THE MAP DANCE

"""
"""
HEURISTICS NOTES

[x] prefer placing houses with the same type together               <- algorithm 1.3 kinda does this automaticly out of necesity
[ ] prefer placing houses which perfectly fit together              <- the "ConfigJudge" will solve this
[ ] prefer placing houses on edges of other houses or water         <- the "random_on_edge" will make this possible
[ ] prefer placing houses so they fit perfectly in AREA boundaries  <- maximize range overlap will solve this
[x] prefer to place as much 'extra free space' off the edge of
    the AREA boundaries                                             <- algorithm 1.3 kinda does this automaticly out of necesity
[ ] group houses, consider them as 1 (moldable) puzzle piece        <- this is on a completely different level, ignore for now

[x] = completed

LOGBOEK
    Jos's HillCLimber Algorithm

    v 1.1:
        - add ring to best house
        - if it doesnt fit
            - random jump 1000 times until valid
                - if still not valid, crash

        NOTE: this doesnt work, the mansion keep on jumping,
        the family homes must move to make place for the large houses

        PERFORMANCE: around 50 ringincreases before getting stuck



    v 1.2:
        - add ring to best house
        - if ONE OF THE OTHER HOUSES DOES NOT FIT ANYMORE
            - random jump THEM 1000 times until valid
                - if still not valid, crash

        NOTE: this also doesnt work, if two mansions clash they still jump around alot for the exact same reason.
              we need something that generally solves an unsolved map
              - its ALOT of work to check all houses in real-time, so much work
                that im tempted to let the map just do another completely random construction

        PERFORMANCE: around 150 ringincreases before getting stuck



    v 1.3:
        - add ring to best house
        - if MAP CONSTRAINTS are not met:
            - PLOT THE COMPLETE MAP AGAIN
            - if A HOUSE OF THE MAP BUILDER TIMES OUT:
                - try building map again,
                - if map builder times out after X iterations, crash

        NOTE: - waarom doe ik dit eigenlijk linear? kan ik niet gwn 400
                iteration situatie pakken en hm een halfuur laten passen??

    OTHER THINGS DONE:
        - added an areConstraintsSatisfied method for map


    v 1.3.1:
        - add ring to best house
        - DONT CHECK IF CORRECT, CONTINUE AT VALUE LEFT OF.
            - if iteration count is new:
                - mark that count as solved
                -

        NOTE: this version is just me changing values around in algorithm 1.3.
              I hardcode a start iteration number, from there on out try to solve that particular iteration.
              Right now I keep track of correct scores, if i implement tara's save and load feature, we could make this parametricly
              Algorithm is response to earlier note: - waarom doe ik dit eigenlijk
              linear? kan ik niet gwn 400 iteration situatie pakken en hm een halfuur laten passen??

              i can let him skip a number with ctrl + c, and he continues better after that.... shall this be implemented algorthmicly??

        PERFORMANCE: 20 house case: up to 312 ringincreases before getting stuck, around 15 mil, water is no problem
                     40 house case: up to 250: around 20 mil  water is correctly fitted in most of the times
                     60 house case: up to 154: around 25 mil, cant correctly fit in water, to fix this, it must be added beforehand or during the fitting in part, not sure how to do that yet



    v 1.4
        - add ring to best house
        - plot the complete map again, IN A SMARTER FASHION: build on edge
        - if a house times out,
            - do similar things as 1.3.1

    OTHER THINGS DONE:
        - TODO added the ConfigJudge, a way of judging the configuration of the houses

        NOTE: not sure how to use the ConfigJudge yet, but being able to judge
        the shapes of houses must be a useful feature

        PERFORMANCE: 20 house case: 420 ringincreases, map value: 16.755.600
                     40 house case: 380 ringincreases, map value: 23.5 mil, water is no problem anymore
                     60 house case: 300 ringincreases, map value: 30.2 mil, water is not a problem anymore too,
                     giving alot of space to mansions free's up enough space for the water squeeze in algorithm to work properly

        EDIT:

        - note when a building is 'done'

    geen beste oplossing garantie
    wel: een erg sterke benadering voor optimaal benutten van vierkante meters

    is dit een soort dijkstra methode?????


        TODO: PROVE THE SMART RING ADDER
        EDIT: daan was completely right, about a fluctuating acual map value.
              the map value calculated by the smart ring adder should be called "guaranteed minimal map value"
              the rings added by the ring adder should be called "guaranteed personal space"



        Not Jos Algorithm v 2.0:
        - start out with 'a' map

        - if the map score improves by moving a house
            - move that house
                - move smart and things, dont go back, iterate, NO random things
            - if all houses cant be improved anymore
                - try house swaps

        - calculate state spaces of moving / swapping
        - calculate what would happen with regards to loops, logical errors, if 1 thing is correct, should it be moved ever again??????

        NOTE: a swap is only meaningful between different types of houses, and if the ring sizes are already hiechi"al, swapping houses NEVER improves the map
        misschien in een vroeg stadium, kijk naar het gebouw met de meeste vrijstandmeters en zorg ervoor dat er een mansion op staat, maar die approach is ongeveer gelijk aan ringen uitdelen aan eerst de mansions

        TODO BOUW EEN ECHTE AFSTANDS CALCULATOR
        bereken eerst a2 + b2
        doe pas de wortel met de grootste


        NOTE: berekningen van hoekpunten is soms iets te gul, er zou in werkelijkheid wand tot wand gerekend moeten worden. we nemen dit als een afrond onnaukeurigheid

"""

from helpers import *

# choose 0, 1 or 2 to get 20, 40 or 60 houses
SELECTED_HOUSE_COUNT = 20 # HOUSE_COUNT[0]


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

    # fill map for first time
    for i in range(SELECTED_HOUSE_COUNT):

        # get current housetype
        ht = housetypelist[i]
        map1.addHouse(ht, (0,0), 0, "random_positions", "non_colliding")

    # ALRORITHM TIME
    # runtime controllers
    MACRO_LIMIT = 500
    LIMIT_MAP_REBUILT = 20000
    LIMIT_HOUSE_RELOCATE = 300

    # algorithm controls
    START_AT = 370
    # PRINT_AT = 1

    # map1.saveJSON("henk.txt")
    # map1.calculateValue()

    # keep increasing the best house
    for i in range(MACRO_LIMIT):

        # smart ring increase process
        selected = map1.findHouseWithMostLandValueRingIncrease()
        houseSelected = map1.house[selected]
        houseSelected.changeRingsBy(1)

        # keep track of counter
        relocatecounter = 0

        # all House Boundaries Minus houseSelected
        otherBounds = [h.boundary for h in map1.house if h is not houseSelected]

        if i < START_AT:
            continue

        # if it does not fit
        if houseSelected.ringboundary.isTouching(otherBounds):

            # try to rebuild the entire map, if that fails, error
            print("rebuilding map. Iteration: {}".format(i))
            if not map1.rebuild(LIMIT_MAP_REBUILT, LIMIT_HOUSE_RELOCATE):
                print("Failed to rebuild at iteration {}, Runtime Error, cannot continue...".format(i))
                # wait for ctrl + c command
                return 0

        # once every x ringincreases, print map
        #if (i % PRINT_AT == 0 and i != 0):
        print("iterations: {}".format(i))

        # enhancements
        tries = 0
        # while(not map1.addWater()):
        #     tries += 1
        #     print("try again. tries = {}".format(tries))
        #     if tries >= 100:
        #         break
        # map1.expandRings()
        map1.saveJSON("henk.txt")
        # map1.expandRings()
        # map1.plot()
        map1.waterBody.clear()

    # enhancements
    # map1.addWater()

    # print value of map
    value = map1.calculateValueEstimate()
    print()
    print("Total map value:", value)

    # werkt dit???


    # draw the map after enhancements
    # map1.plot()

if __name__ == "__main__":
        main()
