#Solution to: http://www.careercup.com/question?id=5726362876772352

from compiler.ast import flatten

data = [[1, 3, 5, 1, 8], 
		[8, 3, 5, 3, 7], 
		[6, 3, 9, 6, 0]] 

pre_computed_solution = {} 

def clip_matrix(data, x1, y1, x2, y2):
	matrix = []
	for i in range(len(data)):
		row = []
		for j in range(len(data[0])):
			if i >= x1 and j >=y1 and i <= x2 and j <= y2:
				row.append(data[i][j])
		matrix.append(row)
	return matrix

if __name__ == "__main__":
	for a in range(len(data)):
		for b in range(len(data[0])):
			for c in range(a+1, len(data)):
				for d in range(b+1, len(data[0])):
					k = "%d-%d-%d-%d" % (a,b,c,d)
					pre_computed_solution[k] = sum(flatten(clip_matrix(data, a, b, c, d)))

	print pre_computed_solution['0-2-2-4']
	print pre_computed_solution['0-0-2-4']
