import numpy as np


class Pool(object):
    """
    A class used to represent a swimming pool - a simulation environment for a robot

    Attributes
    ----------
    length : int
        the length of a pool
    width : int
        the width of a pool
    pollution : floan
        a float number in range [0, 1] which represents the percent of the pool that is polluted
    obstecles : floan
        a float number in range [0, 0.5] which represents the percent of obstecles in the pool
    """

    # TODO
    # try different amount of obstecles
    # try different amount of pollution

    def __init__(self, length=5, width=7, pollution=0.5, obstacles=0.0):
        self.length = length
        self.width = width
        self.pollution = pollution
        self.obstecles = obstacles
        self.grid = np.zeros((self.length, self.width))
        self.render_elems = {-1: 'X', -0.5: 'x', 0: ' ', 1: 'R'}

    def render(self):
        x = '-'
        y = '|'
        z = '  '
        w = ' '
        spaces = 5
        columns = z * spaces + w
        for i in range(self.width):
            columns += 2 * w + str(i) + w
        print(columns)
        row_number = 0
        for j in range(self.length):
            print(z * spaces, x * (self.width * 4 + 1))
            row_print = z * spaces + str(row_number) + y + w
            values = [self.render_elems[val] for val in self.grid[j]]
            for val in values:
                row_print += val + w
                row_print += y + w
            print(row_print)
            row_number += 1
        print(z * spaces, x * (self.width * 4 + 1), '\n')

    def generate_pollution(self):
        pass

    def generate_obstacles(self):
        pass

    def is_clean(self):
        pass
