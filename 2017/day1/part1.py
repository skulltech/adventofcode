def solve(inp):
	sum = 0
	for idx, val in enumerate(inp):
		if (val == inp[int((idx+1) % len(inp))]):
			sum = sum + int(val)
	return sum

def main():
	inp = input('[?] The puzzle input: ')
	print(solve(inp))


if __name__=='__main__':
	main()
