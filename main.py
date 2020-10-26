from env.pool import Pool
from agent import Agent
from policies.random import RandomPolicy


def main():
	pool = Pool(hub_location=[0, 0], seed=42)
	pool.render()

	print('Is the pool clean?', pool.is_clean())

	pool.set_robot_location([0, 1])
	pool.render()

	agent = Agent(policy=RandomPolicy, num_actions=6)


if __name__ == '__main__':
	main()