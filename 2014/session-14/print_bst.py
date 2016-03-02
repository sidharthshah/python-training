#Solution to: http://www.careercup.com/question?id=5665654537453568

import math

def print_bst(depth):
	bst = []
	series = [i for i in range(depth+1)]
	calc_spaces = lambda x: int(math.pow(2, x)) - 1
	spaces = map(calc_spaces, series)

	current_depth = depth
	while current_depth > 0:
		elements = ["*" for i in range( int(math.pow(2, current_depth)) , int(math.pow(2, current_depth+1)))]
		bst.append(elements)
		current_depth -= 1
	bst.append(["*"])
	bst.reverse()

	result = []
	current_depth = depth
	while current_depth > 0:
		line = " " * spaces[depth - current_depth]
		for current_element in bst[current_depth]:
			line += str(current_element) + " " * spaces[depth - current_depth + 1]
		result.append(line)
		current_depth -= 1
	result.reverse()

	print " " * spaces[depth] + "*"
	for line in result:
		print line

if __name__ == "__main__":
	print_bst(6)
