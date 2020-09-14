from env.pool import Pool


def main():
	pool = Pool(hub_location=[0, 0])
	pool.render()

	print('Is the pool clean?', pool.is_clean())

	pool.set_robot_location([1, 1])
	pool.render()


if __name__ == '__main__':
	main()