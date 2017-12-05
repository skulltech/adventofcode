def solve(inp):
	data = [[int(elem) for elem in row.split()] for row in inp.splitlines()]
	sum = 0
	for row in data:
		sum = sum + max(row) - min(row)
	return sum

def main():
	with open('part1-input.txt', 'r') as f:
		inp = f.read()
		print('[*] Reading input from part1-input.txt...')
	print('[*] The solution is: ')
	print(solve(inp))


if __name__=='__main__':
	main()
