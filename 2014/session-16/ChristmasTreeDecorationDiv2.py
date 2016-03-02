#Solution to: http://community.topcoder.com/stat?c=problem_statement&pm=13556&rd=16083

class ChristmasTreeDecorationDiv2:
	def solve(self, color, x, y):
		result = 0
		for i in range(len(x)):
			if color[x[i]-1] != color[y[i]-1]:
				result += 1
		return result

if __name__ == "__main__":
	c = ChristmasTreeDecorationDiv2()
	assert c.solve([1, 2, 3, 3], [1, 2, 3], [2, 3, 4]) == 2
	print c.solve([1, 3, 5], [1, 3], [2, 2])
