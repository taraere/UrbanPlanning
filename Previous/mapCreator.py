"""
Hi christiaan, i made some comments
                                ~ Jos
e"""

class House:
    def __init__(self, x_house, y_house, house_border, house_type):
        """ like i said: lets start thinking in terms of coordinates,
            so as little x and y calling as possible """
        self.x_house = x_house
        self.y_house = y_house
        self.house_border = house_border
        self.house_type = house_type
        # if self.house_type != 'f' or self.house_type != 'b' or self.house_type != 'm':
        #     return


""" een map is niet een extentie van een huis, ik zou dit weghalen"""
class Map(House):

    def __init__(self, x_min_len, y_min_len, x_max_len, y_max_len):
        """ please state the minimum before the maximum """
        self.x_max_len = x_max_len
        self.y_max_len = y_max_len
        self.x_min_len = x_min_len
        self.y_min_len = y_min_len

        self.house_list = []

    def add_house(self):
        """ this does work, this way the house will get attached to a branch """
        self.house_list.append(House)

def main():
    """ ye our code should work like this, good idea """
    main_map = map(160, 180, 0, 0)


if __name__ == "__main__":
     main()
