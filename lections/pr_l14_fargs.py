def func1(num):
	n = num * 5
	print(n)

gnum = 3
func1(gnum)
func1(5)
func1('five')

def func2(n):
	if n < 3:
		n = n * 10
		return n
a = 2
b = func2(a)
print(a)
print(b)

