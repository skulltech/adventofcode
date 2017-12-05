def solve(inp):
	data = [[int(elem) for elem in row.split()] for row in inp.splitlines()]
	sum = 0
	for row in data:
		for i in row:
			for j in row:
				if (i/j).is_integer() and i!=j:
					sum = sum + int(i/j)
	return sum

def main():
	with open('part1-input.txt', 'r') as f:
		inp = f.read()
		print('[*] Reading input from part1-input.txt...')
	print('[*] The solution is: ')
	print(solve(inp))


if __name__=='__main__':
	main()
