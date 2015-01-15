
result = []

for i in range(12):
	row = []
	for j in range(12):
		row.append(i*j)
	result.append(row)

for row in result:
	print "\t".join(map(str, row))
