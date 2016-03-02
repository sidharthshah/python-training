class GoodCompanyDivTwo:
	def countGood(self, superior, workType):
		result = 0
		for i in range(len(superior)):
			department = []
			department.append(i)

			for j in range(i+1, len(superior)):
				if superior[j] == i:
					department.append(j)

			department_work = {}
			for member in department:
				department_work[workType[member]] = 0

			if len(department_work) == len(department):
				result += 1
		return result

if __name__ == "__main__":
	g = GoodCompanyDivTwo()
	assert g.countGood([-1, 0], [1, 2]) == 2
	assert g.countGood([-1, 0], [1, 1]) == 1
	assert g.countGood([-1, 0, 0, 1, 1, 3, 0, 2, 0, 5, 2, 5, 5, 6, 1, 2, 11, 12, 10, 4, 7, 16, 10, 9, 12, 18, 15, 23, 20, 7, 4], [4, 6, 4, 7, 7, 1, 2, 8, 1, 7, 2, 4, 2, 9, 11, 1, 10, 11, 4, 6, 11, 7, 2, 8, 9, 9, 10, 10, 9, 8, 8]) == 27
