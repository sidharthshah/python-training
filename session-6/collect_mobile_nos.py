address = {}
while True:

	print "1. Input Data"
	print "2. Write Data"
	print "3. Read Data"
	print "4. Exit"

	option = raw_input("Please select option:")

	if(int(option) == 1):
		name = raw_input("Enter name:")
		mobile = raw_input("Enter mobile:")
		if len(mobile) != 10:
			print "Invalid Number"
			continue

		if not address.has_key(mobile):
			address[mobile] = name
			print "Added Entry"

		else:
			print "\n\nDuplicate mobile number"
	elif(option == "2"):
		address 
		f = open("address.csv","w")
		for k, v in address.items():
			rec = "%s,%s\n" % (v, k)
			f.write(rec)
		f.close()
		print "File written"
	elif(option == "3"):
		f = open("address.csv","r")
		for line in f.readlines():
			print line
	elif(option == "4"):
		break
	else:
		print "option not valid"
		continue



