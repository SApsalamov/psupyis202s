def myfun():
	print("Функция без параметров")
myfun()

def fib(n):
	print("Последовательность чисел Фиббоначи, не превышающих ", n)
	a, b = 0, 1
	while b < n:
		print(b)
		a, b = b, a + b

fib(100)
fib(200)

def fib2(n):
	print("Числа Фибоначи через return")
	result = []
	a, b = 0, 1
	while b < n:
		result.append(b)
		a, b = b, a + b
	return result
print(fib2(100))

