def getcode(row, column):
	rowfirst = (row*(row-1)/2) + 1
	index = int(rowfirst + sumAP(row+1, column-1))

	code = 20151125
	for i in range(index-1):
		code = nextcode(code)
	return code

def sumAP(first, number):
	return 0.5 * number * (2*first + (number-1))

def nextcode(prevcode):
	return (prevcode*252533) % 33554393


print(getcode(3010, 3019))
