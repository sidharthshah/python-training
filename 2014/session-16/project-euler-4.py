def is_palindrome_num(n):
	x = str(n)
	if x == x[::-1]:
		return True
	return False

max_palindrome = 0

for i in range(111,999):
	for j in range(111, 999):
		if is_palindrome_num(i*j):
			max_palindrome = max(max_palindrome, i*j)

print max_palindrome
