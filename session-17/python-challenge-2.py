def generate_cipher(n):
	result = {}
	for i in range(97, 123):
		j = i + n
		if j >= 123:
			j = 97 + (j - 123)
		result[chr(i)] = chr(j)
	return result

def decrypt(cipher, dictonary):
	result = ""
	for char in cipher:
		if dictonary.has_key(char):
			result += dictonary[char]
		else:
			result += char
	return result

if __name__ == "__main__":
	cipher = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

	print decrypt(cipher, generate_cipher(2))
