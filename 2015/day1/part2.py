def solve(inp):
	floor = 0
	index = 0

	for c in inp:
		index = index + 1
		if (c=='('):
			floor = floor + 1
		elif (c==')'):
			floor = floor - 1
		if (floor==-1):
			return index

def main():
	with open('input.txt', 'r') as f:
		print('[*] Reading input from input.txt...')
		inp = f.read()

	print('[*] The answer is: {}'.format(solve(inp)))


if __name__=='__main__':
	main()
