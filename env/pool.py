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
    obstecles : floan
        a float number in range [0, 0.5] which represents the percent of obstecles in the pool 
    pollution : floan
        a float number in range [0, 1] which represents the percent of the pool that is polluted
	"""


	# TODO 
	# try different amount of obstecles
	# try different amount of pollution

	def __init__(self, length, width, obstecles, pollution):
		self.length = length
		self.width = width
		self.obstecles = obstecles
		self.pollution = pollution
		self.grid = np.zeros((self.length, self.width))

	def generate_pollution(self):
		pass

	def generate_obstecles(self):
		pass

	def is_clean(self):
		pass



		