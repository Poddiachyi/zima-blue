class Robot(object):
	"""
	A class used to represent a robot
	A robot takes one square of the grid world (the swimming pool).

	Robot's sight is similar to human's. 

	If sight = 1 and robot's direction is north

    X X X
	  R

	If sight = 2 and robot's direction is north
	X X X
    X X X
	  R	

	If sight = 2 and robot's direction is east
         X X
	   R X x
	     X x

	direction {north: 0, south: 1, west: 2, east: 3}

	Attributes
    ----------
    battery_capacity : int
        the capacity of robot's battery, an integer number in range [m, n]
    sight : int
        the sight of a robot (how far it sees)
	"""

	# TODO
	# decide on battery_capacity range
	# try different values of battery_capacity 

	def __init__(self, battery_capacity, sight=1):
		self.battery_capacity = battery_capacity
		self.sight = sight
		self.direction = None


	def set_robot_init_direction(self, env):
		hub_location = env.get_hub_location()

		pool_width, pool_height = env.get_pool_size()

		if hub_location[0] == 0:
			self.direction = 3
		elif hub_location[0] == pool_width:
			self.direction = 2
		elif hub_location[1] == 0:
			self.direction = 1
		elif hub_location[1] == pool_height:
			self.direction = 0



	def create_state(self, env):
		observed_pool = self.get_pool_state(env)


	def get_pool_state(self, env):
		robot_x_coord, robot_y_coord = env.get_robot_location()
		pool_width, pool_height = env.get_pool_size()
		if self.direction == 0:
			x1 = max(0, robot_x_coord - 1)
			y1 = max(0, robot_y_coord - 1 - self.sight)

			x2 = min(pool_width, robot_x_coord + 1)
			y2 = max(0, robot_y_coord - 1)

		elif self.direction == 1:
			x1 = max(0, robot_x_coord - 1)
			y1 = min(pool_height, robot_y_coord + 1)

			x2 = min(pool_width, robot_x_coord + 1)
			y2 = min(pool_height, robot_y_coord + 1 + self.sight)

		elif self.direction == 2:
			x1 = min(pool_width, robot_x_coord + 1)
			y1 = max(0, robot_y_coord - 1)

			x2 = min(pool_width, robot_x_coord + self.sight)
			y2 = min(pool_height, robot_y_coord + 1)

		elif self.direction == 3:
			x1 = max(0, robot_x_coord - 1 - self.sight)
			y1 = max(0, robot_y_coord - 1)

			x2 = max(0, robot_x_coord - 1)
			y2 = min(pool_height, robot_y_coord + 1)

		return env.get_observable_pool(x1, y1, x2, y2)






		