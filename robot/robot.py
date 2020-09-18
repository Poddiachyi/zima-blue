class Robot(object):
	"""
	A class used to represent a robot
	A robot takes one square of the grid world (the swimming pool)
	
	Attributes
    ----------
    battery_capacity : int
        the capacity of robot's battery, an integer number in range [m, n]
    sight : int
        the sight of a robot (how far it sees)
    type_of_sight : str 
    	defines how robot sees the world
    	'line':
    		only sees what's right in front of him
    	'cone':
    		sees in a cone like manner, a square right in front of him and both squares on the sides of the first one
    	'around':
    		sees everything around

	"""

	# TODO
	# decide on battery_capacity range
	# try different values of battery_capacity 

	def __init__(self, battery_capacity, sight=1, type_of_sight='cone'):
		self.battery_capacity = battery_capacity
		self.sight = sight


	def set_robot_init_direction(self, env):
		pass


	def create_state(self, env):
		pass





		