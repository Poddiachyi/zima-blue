class Robot(object):
	"""
	A class used to represent a robot
	A robot takes one square of the grid world (the swimming pool)
	
	Attributes
    ----------
    battery_capacity : int
        the capacity of robot's battery, an integer number in range [m, n]
    view : int
        the range of view of a robot
    home_distance : int
        the distance to a charging station (home)
	"""

	# TODO
	# decide on battery_capacity range
	# try different values of battery_capacity 

	def __init__(self, battery_capacity, view, home_distance):
		self.battery_capacity = battery_capacity
		self.view = view
		self.home_distance = home_distance




		