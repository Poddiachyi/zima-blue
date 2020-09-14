import numpy as np
from random import randint, random
from scipy.spatial.distance import euclidean


class Pool(object):
    """
    A class used to represent a swimming pool - a simulation environment for a robot

    Attributes
    ----------
    length : int
        the length of a pool
    width : int
        the width of a pool
    pollution : float
        a float number in range [0, 1] which represents the percent of the pool that is polluted
    obstacles : float
        a float number in range [0, 0.5] which represents the percent of obstacles in the pool
    """

    # TODO
    # try different amount of obstacles
    # try different amount of pollution

    def __init__(self, length=5, width=7, pollution=0.3, obstacles=0.1, hub_location=None):
        self.length = length
        self.width = width
        self.pollution = pollution
        self.obstacles = obstacles
        self.grid = np.zeros((self.length, self.width))
        self.render_elems = {-1: 'Z', -0.5: 'x', 0: ' ', 1: 'R', 2: 'H'}  # obstacle, pollution, clean square of pool, robot, home
        self.hub_location = hub_location
        self.robot_cur_location = hub_location

        
        self.generate_pollution()
        self.generate_obstacles()
        self.place_robot_and_hub()


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
        for i in range(self.length):
            for j in range(self.width):
                if np.random.rand() < self.pollution:
                    self.grid[i][j] = -0.5


    def generate_obstacles(self):
        for i in range(self.length):
            for j in range(self.width):
                if np.random.rand() < self.obstacles:
                    self.grid[i][j] = -1


    def is_clean(self):
        return not -0.5 in self.grid


    def place_robot_and_hub(self):
        if not self.hub_location: 
            # the hub must be on the peripheral
            location = self._gen_random_hub_loc()

            self.hub_location = location
            self.robot_cur_location = location

        self.grid[self.hub_location[0]][self.hub_location[1]] = 1


    def _gen_random_hub_loc(self):
        col_coord = randint(0, self.width - 1)
        row_coord = None
        if col_coord == 0 or col_coord == (self.width - 1):
            row_coord = randint(0, self.length - 1)
        else:
            row_coord = 0 if random() > 0.5 else (self.length - 1)

        return [row_coord, col_coord]


    def set_robot_location(self, location):
        if not self.is_move_possible(location):
            print('Move is not possible')
            return

        if self.are_locations_same(self.robot_cur_location, self.hub_location):
            self.grid[self.hub_location[0]][self.hub_location[1]] = 2 # robot left hub so it should be shown now

        self.grid[location[0]][location[1]] = 1


    def is_move_possible(self, location):
        if self.grid[location[0]][location[1]] == -1: # if there is an obstacle
            return False
        elif self.distance(self.robot_cur_location, location) > 1.5: # distance between two point placed diagonally to one another is about 1.41, that's why
            return False
        return True

    def are_locations_same(self, loc1, loc2):
        return loc1[0] == loc2[0] and loc1[1] == loc2[1]


    def distance(self, point1, point2):
        return euclidean(point1, point2)
