def in_english(num, n):
	remainder = num / n
	eng.append(engDict[remainder])
	eng.append(engDict[n])
	num -= (num / n) * n
	return num

def number_to_english(x):
	engDict = {
	1:"one",
	2:"two",
	3:'three', 
	4:'four', 
	5:'five', 
	6:'six', 
	7:'seven', 
	8:'eight', 
	9:'nine', 
	10:'ten', 
	11:'eleven', 
	12:'twelve', 
	13:'thirteen', 
	14:'fourteen', 
	15:'fifteen', 
	16:'sixteen', 
	17:'seventeen', 
	18:'eighteen', 
	19:'nineteen', 
	20:'twenty', 
	30:'thirty', 
	40:'forty', 
	50:'fifty', 
	60:'sixty', 
	70:'seventy', 
	80:'eighty', 
	90:'ninety', 
	100:'hundred', 
	1000:'thousand', 
	100000:'lac', 
	10000000:'khoka'}
	num = int(x)
	
	while num > 0 :
		eng = []
		if num >= 10000000:
			num = in_english(num ,10000000)
		if num >= 100000:
			num = in_english(num ,100000)
		if num >= 1000:
			num = in_english(num ,1000)
		if num >= 100:
			num = in_english(num ,100)
		if num >= 10:
			eng.append(engDict[num])
			num -= (num / 10) * 10
		if num > 0:	
			eng.append(engDict[num])

	print " ".join(eng)

if __name__ == "__main__":
	number_to_english(40000)