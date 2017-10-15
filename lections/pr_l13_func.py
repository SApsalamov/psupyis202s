def triplesum(a, b, c):
	return a + b + c

print(triplesum(1, 2, 3))

def firstfun():
	print("Firts function")

def secondfun():
	firstfun()
	print("Second funtion")
secondfun()