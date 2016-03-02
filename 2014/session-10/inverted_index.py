import os
import sys
import collections

index = collections.defaultdict(list)
stop_words = []

def index_files(dir_name, files_to_process):
	
	for current_file in files_to_process:

		file_to_read = open(os.path.join(dir_name,current_file))

		for line in file_to_read.readlines():
			line = line.strip()
			line = line.lower()
			for token in line.split():

				if not token in stop_words:
					if current_file not in index[token]:
						index[token].append(current_file)

		print "Indexed file: %s" % current_file

def read_stop_words(file_name):
	file_to_read = open(file_name,"r")

	for line in file_to_read.readlines():
		line = line.strip()
		stop_words.append(line)

def write_index(file_name):
	file_to_write = open(file_name, "w")
	for k,v in index.items():
		rec = "%s\t%s\n" % (k, "\t".join(v))
		file_to_write.write(rec)
	file_to_write.close()

def read_index(file_name):
	file_to_read = open(file_name)
	for line in file_to_read.readlines():
		line = line.strip()
		line = line.split()
		k,v = line[0], line[1:]
		index[k] = v

def print_options():
	print "1: Read Index"
	print "2: Write Index"
	print "3: Index for Input Directory"
	print "4: Search"
	print "5: Quit"

if __name__ == "__main__":

	if len(sys.argv) <= 1:
		print "Please enter a valid directory"
		sys.exit(0)


	dir_name = sys.argv[1]
	read_stop_words("stoplist.txt")

	print_options()
	choice = raw_input("Please enter your choice:")


	while choice != "5":
		if choice == "1":
			file_to_read = raw_input("Please enter name of index to read:")
			read_index(file_to_read)

		if choice == "2":
			file_to_save_name = raw_input("Please enter name of index to write:")
			write_index(file_to_save_name)

		if choice == "3":
			files_to_process = os.listdir(dir_name)
			index_files(dir_name, files_to_process)
			print "Completed Indexing"

		if choice == "4":
			query = raw_input("Please enter the word you want to search:")

			if not index.has_key(query):
				print "%s not found in index" % query
			else:
				print index[query]

		print_options()
		choice = raw_input("Please enter your choice:")			
