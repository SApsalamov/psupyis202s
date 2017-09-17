def sum(a, b=0): # b имеет значение по умолчанию
	c = a + b
	return c
print(sum(2, 3))
print(sum(2))

# args - список аргументов в порядке указания при вызове return args
# тип данных кортеж
def func1(*args):
	return args

print(func1('ddd',111, 222, '4444'))