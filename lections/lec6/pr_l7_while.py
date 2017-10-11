fib1 = 0
fib2 = 1
print (fib1)
print (fib2)
n = 21
i = 0
while i < n:
	fib_sum = fib1 + fib2

	if i > 4:
		print ( "i = ", i, " fib_sum = " ,fib_sum)
	fib1 = fib2
	fib2 = fib_sum
	i = i + 1

i = 0
while i < 21:
	print(i)
	i += 1

i = -1
while i > -21:
	print(i)
	i = i - 3

