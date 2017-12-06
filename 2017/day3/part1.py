import math


def getcoord(index):
	root = math.sqrt(index)
	radius = int(root) if int(root)%2!=0 else int(root) - 1
	count = index - radius*radius
	return int((radius+1)/2), count

def manhattan(index):
	rad, count = getcoord(index)
	arc = abs((count % (rad*2)) - rad)
	return int(arc + rad)


def main():
	inp = input('[?] The puzzle input: ')
	print('[*] The answer is: {}'.format(manhattan(int(inp))))


if __name__=='__main__':
	main()
