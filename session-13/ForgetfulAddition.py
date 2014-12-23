class ForgetfulAddition:
	@classmethod
	def minNumber(self, expression):
		addition = lambda x,y: x + y
		min_sum = int(expression)
		for i in range(len(expression)-1):
			a,b = expression[:len(expression)-i-1], expression[len(expression)-i-1:]
			min_sum = min(min_sum, addition(int(a), int(b)))
		return min_sum

if __name__ == "__main__":
	assert ForgetfulAddition.minNumber("22") == 4
	assert ForgetfulAddition.minNumber("123") == 15
	assert ForgetfulAddition.minNumber("1289") == 101
	assert ForgetfulAddition.minNumber("31415926") == 9067
	assert ForgetfulAddition.minNumber("98765") == 863		