import numpy as np

class RandomPolicy(object):

	def __init__(self, num_actions):
		self.num_actions = num_actions


	def __call__(self, state):
		action_dist = np.random.rand(self.num_actions)
		return action_dist
