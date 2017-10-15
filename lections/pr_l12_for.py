strlist = ['aaaa', 'bbbb', 'cccc', 'dddd']
for s in strlist:
	print(s)

for s in strlist:
	for ch in s:
		print(ch, end='-')
	print()

numlist = [1, 2, 3, 4]
i = 0
for x in numlist:
	numlist[i] = float(x)
	i = i + 1;
print(numlist)