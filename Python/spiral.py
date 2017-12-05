
import numpy as np


SPIRAL_SIZE = 9
INIT_BASE = 1






































def spiral(spiral_size, base):

    if spiral_size < 2:
        stop = np.array(base)
        return stop

    top = spiral_size + base
    new_base = top + spiral_size -1
    matrix = np.array([[i + j for i in range(base, top)] for j in range(spiral_size)])
    part = spiral(spiral_size - 1, new_base)
    if part.size > 1:
        matrix[1:,:-1] = np.flip(np.flip(part, 0), 1)
    else:
        matrix[1:,:-1] = part
    return matrix

def main():
    answer = spiral(SPIRAL_SIZE, INIT_BASE)
    print(answer)


    # base = 1
    # top = SPIRAL_SIZE + base
    # answer = np.array([[i + j for i in range(base, top)] for j in range(SPIRAL_SIZE)])
    # answer[1:,:-1] = 1
    # print(    answer)
if __name__ == "__main__":
    main()
