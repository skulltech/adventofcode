def solution(inp):
	data = [row.split() for row in inp.splitlines()]
	count = 0
	for passphrase in data:
		if len(passphrase) == len(set(passphrase)):
			count = count + 1
	return count

def main():
	with open('input.txt', 'r') as f:
		inp = f.read()
		print('[*] Reading input from input.txt...')
	print('[*] The solution is: ')
	print(solution(inp))


if __name__=='__main__':
	main()
