a = 10
while a != 0:
	print(a)
	a -= 1

print("# Пример с continue и break")
a = 10
while a != 0:
	a -= 1
	if a == 7:
		pass
	if a == 5:
		continue
	if a == 3:
		break
	print(a)
