'''
Beunhaas Architects
by Tara, Christiaan, and Jos

Three main issues presented themselves to us.
1.  Overlapping

    When there are four houses in one block, we can overlap their borders so in the centre of
    the square, they overlap four times from all four houses.

2.  Tetris organisation

    What is the most space-saving way of organising the three house types and the water bodies.

    Shapes of water are either 1, 2, 3, or 4 meters long, and one meter wide.
    You can make a square of 2 until 4 meters squared, and L shapes, but they take space from house perimeters which
    have value (bodies of water doesn't have a value but is necessary).

    Naive Recursive Solution (Dynamic solution to Knap Sac problem).
    Memorize Intermediate Results is one better than that (in speed, compared to the slow solution).
    This stores in array to reuse values.

3.  Ring increase around houses

    This is concerned with how to value adding a meter to around the house and the space you will lose on the corners.
    Comparison between the benefit of losing a quarter of the loss on the corners with the gains you would get from
    the overlapping of four houses (maximum)

Most of all, we have to value different types square meters.
This relationship is what the algorithm will priorisities the scenarios on.
'''
import sys

def main():

    # LARGEst meterage of houses with garden
    gFAMHOME = (8 + (2*2)) * (8 + (2*2))
    gBUNGALOW = (10 + (3*2)) * (7.5 + (3*2))
    gMANSION =  (11 + (6*2)) * (10.5 + (6*2))

    # price of meters squared of water bodies - has value of zero
    pW = 0

    # WORSE prices of houses (m^2)
    pFH = round(285000 /gFAMHOME, 2)
    pB = round(399000 / gBUNGALOW, 2)
    pM = round(610000 / gMANSION, 2)

    # Calculate the value of the plot with certain houses/ in scenario presented

    plot = [
        ['b', 'b', 'bb', 'b', 'b'],
        ['b', 'f', 'bb', 'f', 'b'],
        ['bx', 'bx', 'bbx', 'bx', 'bx'],
        ['x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'c', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x']
        ]

    prices = {
        'b': pFH, 'f': pFH, 'x': pB, 'c': pB, 'n': pM, 'm': pM
    }
    price = 0
    width = 5
    height = 7

    for i in range(height):
        for j in range(width):
            string = plot[i][j]
            for k in string:

                price = price + prices[k]

    print('price: ', round(price, 2))

if __name__ == "__main__":
    main()
