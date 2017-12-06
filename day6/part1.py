def redistribute(banks):
	banks = list(banks)
	val = max(banks)
	idx = banks.index(val)
	banks[idx] = 0

	while val > 0:
		idx = (idx + 1) % len(banks)
		banks[idx] = banks[idx] + 1
		val = val - 1
	return tuple(banks)

def solve(banks):
	states = []
	count = 0

	while True:
		states.append(banks)
		banks = redistribute(banks)
		count = count + 1
		
		if banks in states:
			return count

def main():
	inp = inp('[?] The puzzle input: ')
	print('[*] The answer is: {}'.format(solve(inp)))
