def solve(inp):
	sum = 0
	length = len(inp)

	for idx, val in enumerate(inp):
		cmp = int((idx + (length / 2)) % length)
		if (val == inp[cmp]):
			sum = sum + int(val)
	
	return sum

def main():
	inp = input('[?] The puzzle input: ')
	print(solve(inp))


if __name__=='__main__':
	main()
