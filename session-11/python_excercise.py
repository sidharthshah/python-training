import string
from functools import partial

##Solutions to problems from: http://www.ling.gu.se/~lager/python_exercises.html

def solution_to_7():
	sentence = "I am testing"
	words = sentence.split()
	n = len(words) - 1
	results = []
	for i in range(len(words)):
		words_to_reverse = words[n - i]
		char_to_reverse = [x for x in words_to_reverse]
		char_to_reverse.reverse()
		results.append("".join(char_to_reverse))
	print " ".join(results)

def solution_to_7_easy():
	sentence = "I am testing"
	print sentence[::-1]

def solution_to_8():
	def is_palindrome(x):
		return x == x[::-1]

	print is_palindrome('radar')
	print is_palindrome('prabhu')

def solution_to_9():

	def is_member(x,a):
		return x in a

	numbers = [2,4,5,6,7,8,90]
	# num_to_find = raw_input("Enter a value to find :")
	num_to_find = "90"
	num_to_find = int(num_to_find)

	print is_member(num_to_find, numbers)
	return 

def solution_to_10():

	def overlapping(x, y):
		return len(set(x) & set(y)) >= 1

	print "Solution to 10"
	print overlapping([1,2,3], [3,4,5])
	print overlapping([1,2,3], [9])

def generate_n_chars(c, n):
	return c * n

def solution_to_11():
	print "Solution to 11"
	print generate_n_chars("x", 5)

def solution_to_12():
	def histogram(nums):
		for num in nums:
			print generate_n_chars("*", num)

	print "Solution to 12"
	histogram([10,9,20])

def solution_to_13():
	def max_in_list(x):
		return max(x)

	print "Solution to 13"
	print max_in_list([1,2,3,4,100,0,1000])

def solution_to_14():
	def map_to_lens(words):
		return map(len, words)

	print "Solution to 14"
	print map_to_lens(["jose", "ravi", "vikram", "oankar", "sid", "aniket", "anish"])

def solution_to_15():
	def find_longest_word(words):
		return max(map(len, words))

	print "Solution to 15"
	print find_longest_word(["jose", "ravi", "vikram", "oankar", "sid", "aniket", "anish"])

def solution_to_16():
	def filter_long_words(words, n):
		def is_string_len_n(n, x):
			return len(x) >= n

		filter_valid_strings = partial(is_string_len_n, n)
		return filter(filter_valid_strings, words)
	
	print "Solution to 16"
	print filter_long_words(["jose", "ravi", "vikram", "oankar", "sid", "aniket", "anish"], 5) 

def solution_to_17():
	def clean_punctuation(s):
		exclude = set(string.punctuation)
		s = ''.join(ch for ch in s if ch not in exclude)
		return s

	def is_palindrome(x):
		cleaned_string = clean_punctuation(x)
		cleaned_string = cleaned_string.lower()
		cleaned_string = "".join(cleaned_string.split())

		n = len(cleaned_string) - 1
		for i in range(len(cleaned_string)):
			if cleaned_string[i] != cleaned_string[n-i]:
				return False
		return True

	print "Solution to 17"
	print is_palindrome("Go hang a salami I'm a lasagna hog.")
	print is_palindrome("Sidharth Shah")

if __name__ == "__main__":
	solution_to_7()
	solution_to_7_easy()
	solution_to_8()
	solution_to_9()
	solution_to_10()
	solution_to_11()
	solution_to_12()
	solution_to_13()
	solution_to_14()
	solution_to_15()
	solution_to_16()
	solution_to_17()
