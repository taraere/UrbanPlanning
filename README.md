# UrbanPlanning
Beunhaas Architects
by Tara, Christiaan, and Jos

Week 1
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
    
3.  Ring-increase around houses

    This is concerned with how to value adding a meter to around the house and the space you will lose on the corners.
    Comparison between the benefit of losing a quarter of the loss on the corners with the gains you would get from
    the overlapping of four houses (maximum)
    
Most of all, we have to value different types square meters.
This relationship is what the algorithm will priorisities the scenarios on.

## State Space

The lower bound of our problem is the minimum number of houses required of us without any extra space put around them. 
This value is €7,245,000 with 20 houses without any rings added.

`   # max number of iterations is 50 for placing
    housetypes = initHouseTypes(50)

    # generate correct type parameters
    housetypelist = []
    cumulativeValue = 0
    for ht in housetypelist:
        cumulativeValue += ht.value

    print(cumulativeValue)
`

Our upper bound is harder to calculate. One approximation is to give a mansion (which holds the largest value) the largest number of rings 
on the map which is possible, and push all of the other houses to the edges of map.
