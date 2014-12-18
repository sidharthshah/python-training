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


def print_options():
	print "1: Search"
	print "2: Quit"

if __name__ == "__main__":

	if len(sys.argv) <= 1:
		print "Please enter a valid directory"
		sys.exit(0)


	dir_name = sys.argv[1]
	read_stop_words("stoplist.txt")
	files_to_process = os.listdir(dir_name)
	index_files(dir_name, files_to_process)

	print "Completed Indexing"

	print_options()
	choice = raw_input("Please enter your choice:")


	while choice != "2":
		if choice == "1":
			query = raw_input("Please enter the word you want to search:")

			if not index.has_key(query):
				print "%s not found in index" % query
			else:
				print index[query]

			print_options()
			choice = raw_input("Please enter your choice:")			
