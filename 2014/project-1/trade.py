import commands
import csv
import os.path
from datetime import datetime, timedelta 

URL = "http://www.bseindia.com/download/BhavCopy/Equity/EQ%s_CSV.ZIP"

data = {}

def update_data(row, ts):
	script,open, high, low, close = row[1], row[4], row[5], row[6], row[7]
	script = script.strip()
	if not data.has_key(script):
		data[script] = {}
	data[script][ts] = [open, high, low, close]

if __name__ == "__main__":
	today = datetime.now()
	for i in range(15):
		current_date = today - timedelta(days=i+1)
		TS = "%0.2d%0.2d%s" % (int(str(current_date.day)), int(str(current_date.month)),str(current_date.year)[2:])
		DOWNLOAD_URL = URL % TS
		CMD = "wget %s" % DOWNLOAD_URL
		print "Downloading for %s" % TS
		# s,o = commands.getstatusoutput(CMD)
		read_file = "EQ%s.CSV" % TS
		CMD_UNZIP = "unzip %s" % DOWNLOAD_URL.split("/")[-1] 
		print "Unziping %s" % TS
		status,output = commands.getstatusoutput(CMD_UNZIP)
		print "File Name  = %s" % read_file
		if os.path.isfile(read_file):
			file_to_read = open(read_file,"rb")
			with file_to_read as csvFile:
				csvReader = csv.reader(csvFile, quotechar="|")
				for row in csvReader:
					update_data(row, TS)
		else:
			print read_file+" do not exists"
			continue

	script = raw_input("Enter Script you want to get data of:")
	while script != "-1":
		if not data.has_key(script):
			print "Script Not found"
		else:
			all_ts = data[script].keys()
			all_ts.sort()
			for ts in all_ts:
				print ts,"\t","\t".join(data[script][ts])
		print "\n"
		script = raw_input("Enter Script you want to get data of:")

