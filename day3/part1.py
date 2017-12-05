import math


def manhattan(index):
	root = math.sqrt(index)
	radius = int(root) if int(root)%2!=0 else int(root) - 1
	count = index - radius*radius
	arc = abs((count % (radius+1)) - ((radius+1)/2))

	return int(arc + ((radius+1) / 2))

def main():
	inp = input('[?] The puzzle input: ')
	print(manhattan(int(inp)))


if __name__=='__main__':
	main()
