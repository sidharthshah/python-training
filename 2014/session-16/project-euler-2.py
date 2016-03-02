fib_nums = [1, 2]

is_even = lambda x: x % 2 == 0

while fib_nums[-1] < 4000000:
	if fib_nums[-1] + fib_nums[-2] > 4000000:
		break

	fib_nums.append(fib_nums[-1] + fib_nums[-2])

print sum(filter(is_even, fib_nums))
