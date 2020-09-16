


class Agent(object):

	def __init__(self, policy, num_actions):
		self.policy = policy(num_actions)


	def act(self, state, mask=None):
		action_dist = self.policy(state)

		if mask:
			action_dist = action_dist * np.array(mask)

		return action.argmax()