def agedeterminant(age):
	if age > 0 and age < 7:
		return "You in kindergarten"
	elif age > 6 and age < 19:
		return "You in school"
	elif age > 18 and age < 26:
		return "You in college"
	elif age > 25 and age < 61:
		return "You in work"
	elif age > 60 and age <= 120:
		return "You have the choice"
	elif age <= 0 or age > 120:
		return "Error! This program for humans\n"* 5

print("Society in the early XXI century")


age = int(input("How old are you? - "))
print(agedeterminant(age))