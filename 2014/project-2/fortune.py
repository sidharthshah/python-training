file_to_read = open("fortune.txt")
quotes = []
for line in file_to_read.readlines():
	line = line.strip()
	quotes.append(line)
print quotes
