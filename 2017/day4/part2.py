def isanagram(a, b):
	return sorted(a) == sorted(b)

def valid(passphrase):
	for i, u in enumerate(passphrase):
		for j, v in enumerate(passphrase):
			if i!=j and isanagram(u, v):
				return False
	return True

def solution(inp):
	data = [row.split() for row in inp.splitlines()]
	count = 0
	for passphrase in data:
		if valid(passphrase):
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
