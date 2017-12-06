def solve(inp):
	inp = [int(elem) for elem in inp.split()]
	count = 0
	index = 0

	while index in range(len(inp)):
		val = inp[index]
		inp[index] = inp[index] + 1
		index = val + index
		count = count + 1
	return count


def main():
	with open('input.txt', 'r') as f:
		inp = f.read()
		print('[*] Reading input from input.txt...')
	print('[*] The solution is: {}'.format(solve(inp)))


if __name__=='__main__':
	main()
