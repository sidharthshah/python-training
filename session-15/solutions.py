def solution_3():
	n = int(raw_input("Input N:"))
	return dict([(i, i*i) for i in range(1, n+1)])

def solution_4():
	data = raw_input("Input Data:")
	list_data = list(map(int, data.split(",")))
	tuple_data = tuple(map(int, data.split(",")))

	return list_data, tuple_data

if __name__ == "__main__":
	print solution_3()
	print solution_4()
