x = 0
while(x < 1 or x > 9):
	x = int(input('Enter value between 1 and 9 = '))
	print(x)
	if x >=1 and x <= 3:
		s = input("Enter some string = ")
		n = int(input("Enter number repeat of string = "))
		print(s * n)
	elif x > 3 and x <= 6:
		m = int(input("Enter the power of number = "))
		print(x**m)
	elif x > 6 and x <= 9:
		xplus = x
		i = 1
		while i <= 10:
			xplus = xplus + 1
			print(xplus)
			i = i + 1
	else:
		print("Input error")



