def solve(inp):
	sum = 0
	
	for idx, val in enumerate(inp[:-1]):
		if (val == inp[idx+1]):
			sum = sum + int(val)
	if (inp[0] == inp[-1]):
		sum = sum + int(inp[-1])
	
	return sum

def main():
	inp = input('[?] The puzzle input: ')
	print(solve(inp))


if __name__=='__main__':
	main()
