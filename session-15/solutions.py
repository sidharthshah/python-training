#Solutions to: https://raw.githubusercontent.com/zhiwehu/Python-programming-exercises/master/100+%20Python%20challenging%20programming%20exercises.txt

from collections import defaultdict

def solution_3():
	n = int(raw_input("Input N:"))
	return dict([(i, i*i) for i in range(1, n+1)])

def solution_4():
	data = raw_input("Input Data:")
	list_data = list(map(int, data.split(",")))
	tuple_data = tuple(map(int, data.split(",")))

	return list_data, tuple_data

def solution_5():
	data = raw_input("Input 2 nos. comma seperated:")
	m,n  = data.split(",")
	m,n = int(m), int(n)
	result = []
	for i in range(m):
		row = []
		for j in range(n):
			row.append(i*j)
		result.append(row)
	return result

def solution_8():
	data = raw_input("Input words:")
	data = data.split(",")
	data.sort()
	return data

def solution_10():
	data = raw_input("Input words:")
	words = defaultdict(int)
	for word in data.split(" "):
		words[word] = 0
	uniq_words = words.keys()
	uniq_words.sort()
	return uniq_words

def solution_11():
	data = raw_input("Input numbers:")
	result = []
	for num in data.split(","):
		if int(num, 2) % 5 == 0:
			result.append(num)
	return ",".join(result)

if __name__ == "__main__":
	print solution_3()
	print solution_4()
	print solution_5()
	print solution_8()
	print solution_10()
	print solution_11()
